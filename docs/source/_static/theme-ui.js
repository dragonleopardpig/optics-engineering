/* Small, framework-free enhancements over the official Read the Docs theme. */
(() => {
  "use strict";
  const root = document.documentElement;
  const storageKey = "optics-engineering-appearance";
  const sizeStorageKey = "optics-engineering-text-size";
  const paletteStorageKey = "optics-engineering-palette";
  const TEXT_SIZES = [0.9, 1.0, 1.15, 1.3, 1.45];
  const VALID_PALETTES = [
    "umbriel-cyberpunk",
    "old-paper",
    "modern",
    "original",
    "olo-red",
    "olo-magenta",
    "olo-violet",
    "olo-blue",
    "olo-teal",
    "olo-green",
    "olo-yellow",
    "olo-gray",
  ];
  const system = window.matchMedia("(prefers-color-scheme: dark)");

  function readPreference() {
    try {
      const params = new URLSearchParams(window.location.search);
      const fromUrl = params.get("theme") || (window.location.hash.match(/[#&]theme=([a-z]+)/) || [])[1];
      if (["light", "dark", "system"].includes(fromUrl)) return fromUrl;
    } catch (_) {}
    try {
      const match = window.name && window.name.match(/optics-engineering-appearance=([a-z]+)/);
      if (match && ["light", "dark", "system"].includes(match[1])) return match[1];
    } catch (_) {}
    try {
      const stored = localStorage.getItem(storageKey);
      if (["light", "dark", "system"].includes(stored)) return stored;
    } catch (_) {}
    try {
      const sess = sessionStorage.getItem(storageKey);
      if (["light", "dark", "system"].includes(sess)) return sess;
    } catch (_) {}
    return root.dataset.appearance || "system";
  }

  function readTextSize() {
    try {
      const params = new URLSearchParams(window.location.search);
      const fromUrl = params.get("size");
      if (fromUrl && !isNaN(Number(fromUrl))) return Number(fromUrl);
    } catch (_) {}
    try {
      const match = window.name && window.name.match(/optics-engineering-text-size=([0-9.]+)/);
      if (match && !isNaN(Number(match[1]))) return Number(match[1]);
    } catch (_) {}
    try {
      const stored = localStorage.getItem(sizeStorageKey);
      if (stored && !isNaN(Number(stored))) return Number(stored);
    } catch (_) {}
    try {
      const sess = sessionStorage.getItem(sizeStorageKey);
      if (sess && !isNaN(Number(sess))) return Number(sess);
    } catch (_) {}
    const fromDataset = root.dataset.textSize;
    if (fromDataset && !isNaN(Number(fromDataset))) return Number(fromDataset);
    return 1.0;
  }

  function readPalette() {
    try {
      const params = new URLSearchParams(window.location.search);
      const fromUrl = params.get("palette") || (window.location.hash.match(/[#&]palette=([a-z-]+)/) || [])[1];
      if (VALID_PALETTES.includes(fromUrl)) return fromUrl;
    } catch (_) {}
    try {
      const match = window.name && window.name.match(/optics-engineering-palette=([a-z-]+)/);
      if (match && VALID_PALETTES.includes(match[1])) return match[1];
    } catch (_) {}
    try {
      const stored = localStorage.getItem(paletteStorageKey);
      if (VALID_PALETTES.includes(stored)) return stored;
    } catch (_) {}
    try {
      const sess = sessionStorage.getItem(paletteStorageKey);
      if (VALID_PALETTES.includes(sess)) return sess;
    } catch (_) {}
    return root.dataset.palette || "umbriel-cyberpunk";
  }

  let preference = readPreference();
  let currentTextSize = readTextSize();
  let currentPalette = readPalette();

  function syncLinks(currentPref = preference, currentSize = currentTextSize, currentPal = currentPalette) {
    if (window.location.protocol !== "file:") return;
    document.querySelectorAll("a[href]").forEach(link => {
      const rawHref = link.getAttribute("href");
      if (!rawHref || rawHref.startsWith("#") || rawHref.startsWith("http:") || rawHref.startsWith("https:") || rawHref.startsWith("mailto:") || rawHref.startsWith("javascript:")) return;
      try {
        const url = new URL(link.href);
        if (currentPref === "system") {
          url.searchParams.delete("theme");
        } else {
          url.searchParams.set("theme", currentPref);
        }
        if (currentSize === 1.0) {
          url.searchParams.delete("size");
        } else {
          url.searchParams.set("size", String(currentSize));
        }
        if (currentPal === "umbriel-cyberpunk") {
          url.searchParams.delete("palette");
        } else {
          url.searchParams.set("palette", currentPal);
        }
        link.href = url.href;
      } catch (_) {}
    });
  }

  function applyAppearance(value, persist = false) {
    preference = ["light", "dark", "system"].includes(value) ? value : "system";
    root.dataset.appearance = preference;
    root.dataset.theme = preference === "dark" || (preference === "system" && system.matches) ? "dark" : "light";
    document.querySelectorAll("button[data-appearance]").forEach(button => {
      button.setAttribute("aria-pressed", String(button.dataset.appearance === preference));
    });
    if (persist) {
      try { localStorage.setItem(storageKey, preference); } catch (_) { /* Private storage may be unavailable. */ }
      try { sessionStorage.setItem(storageKey, preference); } catch (_) {}
      try {
        const cleanName = (window.name || "").replace(/(^|;)optics-engineering-appearance=[a-z]+/, "");
        window.name = cleanName ? `${cleanName};optics-engineering-appearance=${preference}` : `optics-engineering-appearance=${preference}`;
      } catch (_) {}
      syncLinks(preference, currentTextSize, currentPalette);
    }
  }

  function applyTextSize(size, persist = false) {
    const clamped = TEXT_SIZES.reduce((prev, curr) => Math.abs(curr - size) < Math.abs(prev - size) ? curr : prev, 1.0);
    currentTextSize = clamped;
    root.style.setProperty("--text-scale", String(clamped));
    root.dataset.textSize = String(clamped);

    const indicator = document.querySelector("[data-role='text-size-value']");
    if (indicator) {
      indicator.textContent = `${Math.round(clamped * 100)}%`;
    }

    const decBtn = document.querySelector("button[data-text-size='decrease']");
    const incBtn = document.querySelector("button[data-text-size='increase']");
    const resetBtn = document.querySelector("button[data-text-size='reset']");
    const idx = TEXT_SIZES.indexOf(clamped);
    if (decBtn) decBtn.disabled = idx <= 0;
    if (incBtn) incBtn.disabled = idx >= TEXT_SIZES.length - 1;
    if (resetBtn) resetBtn.setAttribute("aria-pressed", String(clamped === 1.0));

    if (persist) {
      try { localStorage.setItem(sizeStorageKey, String(clamped)); } catch (_) {}
      try { sessionStorage.setItem(sizeStorageKey, String(clamped)); } catch (_) {}
      try {
        const cleanName = (window.name || "").replace(/(^|;)optics-engineering-text-size=[0-9.]+/, "");
        window.name = cleanName ? `${cleanName};optics-engineering-text-size=${clamped}` : `optics-engineering-text-size=${clamped}`;
      } catch (_) {}
      syncLinks(preference, currentTextSize, currentPalette);
    }
  }

  function applyPalette(value, persist = false) {
    currentPalette = VALID_PALETTES.includes(value) ? value : "umbriel-cyberpunk";
    root.dataset.palette = currentPalette;
    const picker = document.querySelector("select[data-palette-picker]");
    if (picker && picker.value !== currentPalette) {
      picker.value = currentPalette;
    }
    if (persist) {
      try { localStorage.setItem(paletteStorageKey, currentPalette); } catch (_) {}
      try { sessionStorage.setItem(paletteStorageKey, currentPalette); } catch (_) {}
      try {
        const cleanName = (window.name || "").replace(/(^|;)optics-engineering-palette=[a-z-]+/, "");
        window.name = cleanName ? `${cleanName};optics-engineering-palette=${currentPalette}` : `optics-engineering-palette=${currentPalette}`;
      } catch (_) {}
      try {
        const currentUrl = new URL(window.location.href);
        if (currentPalette === "umbriel-cyberpunk") {
          currentUrl.searchParams.delete("palette");
        } else {
          currentUrl.searchParams.set("palette", currentPalette);
        }
        window.history.replaceState(null, "", currentUrl.href);
      } catch (_) {}
      syncLinks(preference, currentTextSize, currentPalette);
    }
  }

  function changeTextSize(delta) {
    const idx = TEXT_SIZES.indexOf(currentTextSize);
    const nextIdx = Math.max(0, Math.min(TEXT_SIZES.length - 1, (idx === -1 ? 1 : idx) + delta));
    applyTextSize(TEXT_SIZES[nextIdx], true);
  }

  function init() {
    applyAppearance(preference);
    applyTextSize(currentTextSize);
    applyPalette(currentPalette);
    syncLinks(preference, currentTextSize, currentPalette);
    document.querySelectorAll("button[data-appearance]").forEach(button => {
      button.addEventListener("click", () => applyAppearance(button.dataset.appearance, true));
    });
    const decBtn = document.querySelector("button[data-text-size='decrease']");
    if (decBtn) decBtn.addEventListener("click", () => changeTextSize(-1));
    const incBtn = document.querySelector("button[data-text-size='increase']");
    if (incBtn) incBtn.addEventListener("click", () => changeTextSize(1));
    const resetBtn = document.querySelector("button[data-text-size='reset']");
    if (resetBtn) resetBtn.addEventListener("click", () => applyTextSize(1.0, true));

    const picker = document.querySelector("select[data-palette-picker]");
    if (picker) {
      picker.value = currentPalette;
      picker.addEventListener("change", () => applyPalette(picker.value, true));
    }

    system.addEventListener("change", () => { if (preference === "system") applyAppearance("system"); });
    window.addEventListener("storage", event => {
      if (event.key === storageKey) applyAppearance(event.newValue || "system");
      if (event.key === sizeStorageKey && event.newValue) applyTextSize(Number(event.newValue));
      if (event.key === paletteStorageKey && event.newValue) applyPalette(event.newValue);
    });

    const search = document.querySelector(".sidebar-search input[name='q']");
    const shortcut = document.querySelector(".sidebar-search kbd");
    if (shortcut) shortcut.textContent = /Mac|iPhone|iPad/.test(navigator.platform) ? "⌘ K" : "Ctrl K";
    const sidebar = document.querySelector(".wy-nav-side");
    const menuButton = document.querySelector("[data-menu-toggle]");
    if (sidebar) { sidebar.id = "site-navigation"; sidebar.setAttribute("aria-label", "Documentation navigation"); }
    function setMenu(open, restore = false) {
      document.body.classList.toggle("nav-open", open);
      if (sidebar) sidebar.classList.toggle("shift", open);
      if (menuButton) {
        menuButton.setAttribute("aria-expanded", String(open));
        menuButton.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
      }
      if (open && sidebar) {
        const target = search || sidebar.querySelector("a");
        if (target) target.focus();
      } else if (restore && menuButton) menuButton.focus();
    }
    if (menuButton) menuButton.addEventListener("click", () => setMenu(!document.body.classList.contains("nav-open")));
    const scrim = document.querySelector("[data-menu-close]");
    if (scrim) scrim.addEventListener("click", () => setMenu(false, true));
    document.addEventListener("keydown", event => {
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k" && search) {
        event.preventDefault();
        if (window.matchMedia("(max-width: 899px)").matches) setMenu(true);
        search.focus();
        search.select();
      }
      if (event.key === "Escape" && document.body.classList.contains("nav-open")) {
        event.preventDefault();
        setMenu(false, true);
      }
      if (event.key === "Tab" && document.body.classList.contains("nav-open") && sidebar) {
        const focusable = Array.from(sidebar.querySelectorAll("a[href],button:not([disabled]),input:not([type=hidden])"))
          .filter(element => element.getClientRects().length);
        const first = focusable[0], last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
      }
    });
    window.matchMedia("(min-width: 900px)").addEventListener("change", event => { if (event.matches) setMenu(false); });

    const copyIcon = '<svg class="ui-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V4a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v11a1 1 0 0 0 1 1h4"/></svg>';
    const checkIcon = '<svg class="ui-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 4 4L19 6"/></svg>';
    async function copy(text) {
      if (navigator.clipboard && window.isSecureContext) { await navigator.clipboard.writeText(text); return; }
      const area = document.createElement("textarea");
      area.value = text;
      area.style.cssText = "position:fixed;left:-9999px;top:0";
      document.body.appendChild(area);
      area.select();
      const success = document.execCommand("copy");
      area.remove();
      if (!success) throw new Error("Clipboard access was denied");
    }
    document.querySelectorAll("div[class*='highlight-']").forEach(block => {
      const pre = block.querySelector(".highlight pre");
      if (!pre || block.querySelector(".copy-button")) return;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "copy-button";
      button.setAttribute("aria-label", "Copy code to clipboard");
      button.title = "Copy code";
      button.innerHTML = copyIcon;
      button.addEventListener("click", async () => {
        try {
          await copy(pre.innerText.replace(/\n$/, ""));
          button.innerHTML = checkIcon;
          button.dataset.copied = "true";
          button.setAttribute("aria-label", "Code copied");
          document.getElementById("copy-status").textContent = "Code copied to clipboard.";
          setTimeout(() => { button.innerHTML = copyIcon; delete button.dataset.copied; button.setAttribute("aria-label", "Copy code to clipboard"); }, 1800);
        } catch (_) {
          document.getElementById("copy-status").textContent = "Could not copy. Select the code and copy it manually.";
        }
      });
      block.appendChild(button);
    });

    const toc = document.querySelector(".page-toc");
    if (toc && "IntersectionObserver" in window) {
      const links = Array.from(toc.querySelectorAll('a[href^="#"]'));
      const observer = new IntersectionObserver(entries => {
        const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (!visible.length) return;
        const id = visible[0].target.id;
        links.forEach(link => {
          const current = decodeURIComponent(link.hash.slice(1)) === id;
          link.classList.toggle("is-active", current);
          if (current) link.setAttribute("aria-current", "location"); else link.removeAttribute("aria-current");
        });
      }, { rootMargin: "-15% 0px -65% 0px", threshold: 0 });
      document.querySelectorAll("main section[id], main dt[id]").forEach(section => observer.observe(section));
    }
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
