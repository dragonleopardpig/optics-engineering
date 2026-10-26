from __future__ import annotations

import re


LABELS = {
    "wₓ = a/2": r"w_x=\frac{a}{2}",
    "wᵧ = a/2": r"w_y=\frac{a}{2}",
    "δνₓ = 1/wₓ": r"\delta\nu_x=\frac{1}{w_x}",
    "δνᵧ = 1/wᵧ": r"\delta\nu_y=\frac{1}{w_y}",
    "M ≤ (B wₓ)(B wᵧ) = (Ba)²/4": r"M\leq(Bw_x)(Bw_y)=\frac{(Ba)^2}{4}",
    "ML ≤ (Ba)²": r"ML\leq(Ba)^2",
    "[[1,t/n],[0,1]]": r"\begin{pmatrix}1&\frac{t}{n}\\0&1\end{pmatrix}",
    "[[1,0],[-P,1]]": r"\begin{pmatrix}1&0\\-P&1\end{pmatrix}",
    "[[1,0],[2n/r,1]]": r"\begin{pmatrix}1&0\\\frac{2n}{r}&1\end{pmatrix}",
    "[[1,0],[-1/f,1]]": r"\begin{pmatrix}1&0\\-\frac{1}{f}&1\end{pmatrix}",
    "[[0,f],[-1/f,0]]": r"\begin{pmatrix}0&f\\-\frac{1}{f}&0\end{pmatrix}",
    "[[m,0],[-1/f,1/m]]": r"\begin{pmatrix}m&0\\-\frac{1}{f}&\frac{1}{m}\end{pmatrix}",
    "[[m,0],[0,1/m]]": r"\begin{pmatrix}m&0\\0&\frac{1}{m}\end{pmatrix}",
    "dN/dt = (N0−N)/tsp − (N/Nt)(n/tp)": r"\frac{\mathrm{d}N}{\mathrm{d}t}=\frac{N_0-N}{t_{\mathrm{sp}}}-\frac{N}{N_t}\frac{n}{t_p}",
    "M² > 1: z_R = π w₀² / (M² λ), θ = M² λ / (π w₀), w₀ θ = M² λ / π": r"M^2>1:\quad z_R=\frac{\pi w_0^2}{M^2\lambda},\quad\theta=\frac{M^2\lambda}{\pi w_0},\quad w_0\theta=\frac{M^2\lambda}{\pi}",
    "Working F-number N_w ≈ N (1 + |m|) for unit pupil magnification": r"\text{Working f-number}\qquad N_{\mathrm{w}}\approx N(1+|m|)\quad\text{(unit pupil magnification)}",
    "macro example: N = 4 at |m| = 1 → N_w = 8 → Airy diameter ≈ 10.7 µm at λ = 0.55 µm": r"N=4,\quad |m|=1:\quad N_{\mathrm{w}}=8,\qquad d_{\mathrm{Airy}}\approx10.7\,\mu\mathrm{m}\quad(\lambda=0.55\,\mu\mathrm{m})",
    "D = 2 w_in is the incident beam diameter; check aperture clipping": r"D=2w_{\mathrm{in}}\qquad\text{incident }1/e^2\text{ beam diameter; check aperture clipping}",
    "τ1 ≪ tsp": r"\tau_1\ll t_{\mathrm{sp}}",
    "Steady lasing gives N = Nt and nss = (N0 − Nt)tp/tsp, twice the three-level value.": r"\text{Steady lasing:}\quad N=N_t,\qquad n_{\mathrm{ss}}=\frac{(N_0-N_t)t_p}{t_{\mathrm{sp}}}\qquad\text{(twice the three-level value)}",
    "Delta x = 2 f_a tau": r"\Delta x=2f_a\tau",
    "spacing / wavelength = 0.5": r"\frac{\text{spacing}}{\lambda}=0.5",
    "spacing / wavelength = 2": r"\frac{\text{spacing}}{\lambda}=2",
    "Thin-lens imaging — 1/s + 1/s' = 1/f": r"\text{Thin-lens imaging}\qquad \frac{1}{s}+\frac{1}{s'}=\frac{1}{f}",
    "m = y'/y = −s'/s (sign keeps the inverted-image convention)": r"m=\frac{y'}{y}=-\frac{s'}{s}\qquad\text{(inverted-image sign convention)}",
    "f-number N = f / D (cone half-angle ≈ 1/(2N))": r"\text{f-number}\quad N=\frac{f}{D}\qquad\text{cone half-angle}\approx\frac{1}{2N}",
    "Airy disk diameter d ≈ 2.44 λ N Diffraction MTF cutoff ν_c = 1/(λ N)": r"\text{Airy diameter}\quad d\approx2.44\lambda N\qquad\text{MTF cutoff}\quad\nu_c=\frac{1}{\lambda N}",
    "Depth of field DoF ≈ 2 N c (1 + |m|) / m²": r"\text{Depth of field}\qquad\mathrm{DoF}\approx\frac{2Nc(1+|m|)}{m^2}",
    "distant focus → hyperfocal H ≈ f² / (N c) + f DoF behind ≈ 2× DoF in front (for moderate s)": r"\text{Hyperfocal distance}\quad H\approx\frac{f^2}{Nc}+f",
    "Hyperfocal distance H ≈ f²/(N c) + f": r"\text{Hyperfocal distance}\qquad H\approx\frac{f^2}{Nc}+f",
    "focus at H → sharpness extends from H/2 to ∞": r"\text{Focus at }H\quad\Longrightarrow\quad\text{sharpness from }\frac{H}{2}\text{ to }\infty",
    "sharp zone: H/2 … ∞": r"\text{Sharp zone:}\quad\frac{H}{2}\;\ldots\;\infty",
    "H/2": r"\frac{H}{2}",
    "focus s < H → near limit ≈ s·H / (H + s − f) far limit ≈ s·H / (H − s + f) (or ∞ when s ≥ H)": r"s<H:\quad s_{\mathrm{near}}\approx\frac{sH}{H+s-f}\qquad s_{\mathrm{far}}\approx\frac{sH}{H-s+f}",
    "Angle of view AFOV = 2 atan( d / (2 f) )": r"\text{Angle of view}\qquad\mathrm{AFOV}=2\arctan\!\left(\frac{d}{2f}\right)",
    "Diffraction limit: d_Airy = 2.44 λ N": r"\text{Diffraction limit:}\qquad d_{\mathrm{Airy}}=2.44\lambda N",
    "Rayleigh-resolvable angular separation Δθ = 1.22 λ / D": r"\text{Rayleigh angular separation}\qquad\Delta\theta=1.22\frac{\lambda}{D}",
    "Pixel sampling — Nyquist ν_pix = 1 / (2 p)": r"\text{Pixel sampling --- Nyquist}\qquad\nu_{\mathrm{pix}}=\frac{1}{2p}",
    "ν_c = 1/(λN)": r"\nu_c=\frac{1}{\lambda N}",
    "ν_pix = 1/(2p)": r"\nu_{\mathrm{pix}}=\frac{1}{2p}",
    "good rule: N ≈ p / (λ · k) with k ≈ 1–2 → pixel ≈ Airy radius for diffraction-limited match": r"N\approx\frac{p}{\lambda k},\quad k\approx1\text{--}2\qquad\text{diffraction and pixel sampling trade-off}",
    "Snell: n₁ sin θ₁ = n₂ sin θ₂ TIR: θ_c = arcsin(n₂ / n₁)": r"\text{Snell: }n_1\sin\theta_1=n_2\sin\theta_2\qquad\text{TIR: }\theta_c=\arcsin\!\left(\frac{n_2}{n_1}\right)",
    "Two thin lenses, separation d: 1/f = 1/f₁ + 1/f₂ − d / (f₁ f₂)": r"\text{Two thin lenses:}\qquad\frac{1}{f}=\frac{1}{f_1}+\frac{1}{f_2}-\frac{d}{f_1f_2}",
    "P = P₁ + P₂ − d P₁ P₂ (powers add, then subtract the gap term)": r"P=P_1+P_2-dP_1P_2\qquad\text{(including the separation term)}",
    "d = 0 → 1/f = 1/f₁ + 1/f₂ d = f₁ + f₂ → afocal telescope, magnification M = −f₁/f₂": r"d=0:\ \frac{1}{f}=\frac{1}{f_1}+\frac{1}{f_2}\qquad d=f_1+f_2:\ \text{afocal},\ M=-\frac{f_1}{f_2}",
    "1:1 macro rule s = s' = 2f (between principal planes)": r"\text{1:1 macro imaging}\qquad s=s'=2f\quad\text{(principal-plane distances)}",
    "working distance ≈ 2f − front-vertex offset ; W.D. ≈ f(1 + 1/m) for m < 1": r"\text{At 1:1: working distance}\approx2f-\text{front-vertex offset}",
    "working F-number N_w = N (1 + |m|) = 2N at 1:1 → doubles effective f-number": r"N_{\mathrm{w}}\approx N(1+|m|)=2N\quad\text{at 1:1, for unit pupil magnification}",
    "Gaussian beam w(z) = w₀ √(1 + (z / z_R)²)": r"\text{Gaussian beam}\qquad w(z)=w_0\sqrt{1+\left(\frac{z}{z_R}\right)^2}",
    "z_R = π w₀² / λ far-field half-angle θ = λ / (π w₀)": r"z_R=\frac{\pi w_0^2}{\lambda}\qquad\text{far-field half-angle}\quad\theta=\frac{\lambda}{\pi w_0}",
    "w₀√2": r"w_0\sqrt{2}",
    "θ → λ/(πw₀)": r"\theta\longrightarrow\frac{\lambda}{\pi w_0}",
    "M² > 1 multiplies both zR and θ; the beam-parameter product is w₀·θ = (M²) · λ/π": r"M^2>1:\quad z_R=\frac{\pi w_0^2}{M^2\lambda},\quad\theta=\frac{M^2\lambda}{\pi w_0},\quad w_0\theta=\frac{M^2\lambda}{\pi}",
    "Focused spot 2 w_f ≈ (4 λ / π) · (f / D) = (4/π) · λ · N": r"\text{Focused Gaussian spot}\qquad2w_f\approx\frac{4\lambda}{\pi}\frac{f}{D}=\frac{4}{\pi}\lambda N",
    "tightest focus when D fills the lens aperture (D = w_in beam diameter on lens)": r"D=2w_{\mathrm{in}}\qquad\text{incident }1/e^2\text{ beam diameter; check aperture clipping}",
    "depth of focus 2 z_R = 2 π w_f² / λ Power density I_0 = 2 P / (π w_f²)": r"\text{Depth of focus}\quad2z_R=\frac{2\pi w_f^2}{\lambda}\qquad I_0=\frac{2P}{\pi w_f^2}",
    "Two-mirror cavity stability 0 ≤ g₁ g₂ ≤ 1, g_i = 1 − L/R_i": r"\text{Two-mirror cavity:}\quad0\le g_1g_2\le1,\qquad g_i=1-\frac{L}{R_i}",
    "Working F-number N_w = N · (1 + |m|) (and N_w = N / (1 − m) for s in front)": r"\text{Working f-number}\qquad N_{\mathrm{w}}\approx N(1+|m|)\quad\text{(unit pupil magnification)}",
    "1/(2 N_w) = sin u' → effective f-number grows with magnification": r"N_{\mathrm{w}}\approx\frac{1}{2\sin u'}\qquad\text{the image-side cone narrows as magnification grows}",
    "macro example: N = f/4 at m = 1 → N_w = 8 → diffraction Airy ≈ 5.4 µm @ 0.55 µm": r"N=4,\quad |m|=1:\quad N_{\mathrm{w}}=8,\qquad d_{\mathrm{Airy}}\approx10.7\,\mu\mathrm{m}\quad(\lambda=0.55\,\mu\mathrm{m})",
    "J = [[4, 1], [1, 3]] pixels/µm; measured e = (7, −1) pixels; γ = 0.5": r"J=\left(\begin{smallmatrix}4&1\\1&3\end{smallmatrix}\right)\frac{\mathrm{pixels}}{\mu\mathrm{m}},\quad\boldsymbol{e}=(7,-1)\,\mathrm{pixels},\quad\gamma=0.5",
    "Retained coupling η / η₀ (%)": r"\text{Retained coupling}\quad\eta/\eta_0\quad(\%)",
    "θ = ∠(−d, n) = ∠(dr, n)": r"\theta=\angle(-\boldsymbol{d},\boldsymbol{n})=\angle(\boldsymbol{d}_{r},\boldsymbol{n})",
    "d∥ = d − (d · n)n": r"\boldsymbol{d}_{\parallel}=\boldsymbol{d}-(\boldsymbol{d}\cdot\boldsymbol{n})\boldsymbol{n}",
    "d⊥ = (d · n)n": r"\boldsymbol{d}_{\perp}=(\boldsymbol{d}\cdot\boldsymbol{n})\boldsymbol{n}",
    "d = d∥ + d⊥": r"\boldsymbol{d}=\boldsymbol{d}_{\parallel}+\boldsymbol{d}_{\perp}",
    "dr = d∥ − d⊥": r"\boldsymbol{d}_r=\boldsymbol{d}_{\parallel}-\boldsymbol{d}_{\perp}",
    "dr = d − 2(d · n)n": r"\boldsymbol{d}_r=\boldsymbol{d}-2(\boldsymbol{d}\cdot\boldsymbol{n})\boldsymbol{n}",
    "Wfootprint = W / |cos θ|": r"W_{\mathrm{footprint}}=\frac{W}{|\cos\theta|}",
    "Cfold = A |cos θ| — projected clear width": r"C_{\mathrm{fold}}=A|\cos\theta|\qquad\text{projected clear width}",
    "Wfootprint = Wf / |cos θ| = 30 / cos 45°": r"W_{\mathrm{footprint}}=\frac{W_f}{|\cos\theta|}=\frac{30}{\cos45^\circ}",
    "Ωout = disk ∩ rectangle — not an ellipse": r"\Omega_{\mathrm{out}}=\mathrm{disk}\cap\mathrm{rectangle}\qquad\text{(not an ellipse)}",
    "support: Ωobject ≈ Ωsource ⊕ disk(L tan α); hemisphere → unbounded": r"\Omega_{\mathrm{object}}\approx\Omega_{\mathrm{source}}\oplus\mathrm{disk}(L\tan\alpha)\quad\text{(finite cone)}",
    "E(P) = ∫ Le(s→P) T(s,P) cos θs cos θP / r² dAs — s runs over the visible source area Avisible": r"E(P)=\int_{A_{\mathrm{visible}}}L_e(s\to P)\,T(s,P)\,\frac{\cos\theta_s\cos\theta_P}{r^2}\,\mathrm{d}A_s",
    "(39 − 35) / 2 ≈ 2 mm per side": r"\frac{39-35}{2}\approx2\,\mathrm{mm}\quad\text{per side}",
    "Aequivalent = 35 / cos 45° ≈ 49.50 mm (45°-plane proxy, not a stop)": r"A_{\mathrm{equivalent}}=\frac{35}{\cos45^\circ}\approx49.50\,\mathrm{mm}\quad\text{(tilted-plane proxy)}",
    "f = A_spot / A_pixel = 1%": r"f=\frac{A_{\mathrm{spot}}}{A_{\mathrm{pixel}}}=1\%",
    "B(T_hot)/B(T_bg)": r"\frac{B(T_{\mathrm{hot}})}{B(T_{\mathrm{bg}})}",
    "|ρₛ| = ½ |ε| d₂ D": r"|\rho_s|=\frac{1}{2}|\varepsilon|d_2D",
    "ρₛ = 1.22 λd₂ / D": r"\rho_s=1.22\frac{\lambda d_2}{D}",
    "u₀(y) (µm⁻¹ᐟ²)": r"u_0(y)\quad(\mu\mathrm{m}^{-1/2})",
    "ℓ₁ = √(d₁² + x²)": r"\ell_1=\sqrt{d_1^2+x^2}",
    "ℓ₂ = √(d₂² + (d − x)²)": r"\ell_2=\sqrt{d_2^2+(d-x)^2}",
    "P = E/(ητ)": r"P=\frac{E}{\eta\tau}",
    "E₁ = [Eₓ, Eᵧ]ᵀ": r"\boldsymbol{E}_1=(E_x,E_y)^{\mathsf{T}}",
    "I = E₂†E₂": r"I=\boldsymbol{E}_2^\dagger\boldsymbol{E}_2",
    "S₁ = [I,Q,U,V]ᵀ": r"\boldsymbol{S}_1=(I,Q,U,V)^{\mathsf{T}}",
    "State₂ = Mₙ ··· M₂ M₁ State₁ (rightmost factor acts first)": r"\boldsymbol{s}_2=M_n\cdots M_2M_1\boldsymbol{s}_1\qquad\text{(rightmost factor first)}",
    "Ray vector (y, nθ)ᵀ — rightmost matrix acts first": r"\text{Ray vector }(y,n\theta)^{\mathsf{T}}\qquad\text{rightmost matrix acts first}",
    "[ 1 t/n ]": r"\left[\;1\quad\frac{t}{n}\;\right]",
    "[2n/r 1 ]": r"\left[\;\frac{2n}{r}\quad1\;\right]",
    "[-1/f 1 ]": r"\left[\;-\frac{1}{f}\quad1\;\right]",
    "[-1/f 0 ]": r"\left[\;-\frac{1}{f}\quad0\;\right]",
    "[-1/f 1/m]": r"\left[\;-\frac{1}{f}\quad\frac{1}{m}\;\right]",
    "[0 1/m]": r"\left[\;0\quad\frac{1}{m}\;\right]",
    "Half-trace s = (A + D)/2": r"\text{Half-trace}\quad s=\frac{A+D}{2}",
    "s > 1: λ = exp(±τ)": r"s>1:\quad\lambda=e^{\pm\tau}",
    "|s| < 1: λ = exp(±iθ)": r"|s|<1:\quad\lambda=e^{\pm i\theta}",
    "cos θ = s, sin θ = √(1 − s²)": r"\cos\theta=s,\qquad\sin\theta=\sqrt{1-s^2}",
    "q = (Aq + B)/(Cq + D)": r"q=\frac{Aq+B}{Cq+D}",
    "w₀² = − λ sinθ /(πC)": r"w_0^2=-\frac{\lambda\sin\theta}{\pi C}",
    "E(eV) = 1240 / wavelength(nm)": r"E\,(\mathrm{eV})=\frac{1240}{\lambda\,(\mathrm{nm})}",
    "recombination Δn / τ": r"\text{recombination}\quad\frac{\Delta n}{\tau}",
    "Carrier concentration, N_D (cm^-3)": r"\text{Carrier concentration, }N_D\quad(\mathrm{cm}^{-3})",
    "C/A (F cm^-2)": r"\frac{C}{A}\quad(\mathrm{F}\,\mathrm{cm}^{-2})",
    "Drive current, J_2 / J_th (log scale)": r"\text{Drive current, }\frac{J_2}{J_{\mathrm{th}}}\quad\text{(log scale)}",
    "f/2": r"f/2",
    "f/5.6": r"f/5.6",
    "f/8": r"f/8",
    "time average = 1/2": r"\text{time average}=\frac{1}{2}",
    "round-trip OPL = 2nt cos θt": r"\mathrm{OPL}_{\mathrm{round\ trip}}=2nt\cos\theta_t",
    "FWHM = 0.885893 × λL/a": r"\mathrm{FWHM}=0.885893\frac{\lambda L}{a}",
    "edge: I/I0 = 1/4": r"\text{edge:}\quad\frac{I}{I_0}=\frac{1}{4}",
    "dN/dt = R − N/tsp − WiN": r"\frac{\mathrm{d}N}{\mathrm{d}t}=R-\frac{N}{t_{\mathrm{sp}}}-W_iN",
    "Wi = n/(Nttp)": r"W_i=\frac{n}{N_t t_p}",
    "dN/dt = (N0−N)/tsp": r"\frac{\mathrm{d}N}{\mathrm{d}t}=\frac{N_0-N}{t_{\mathrm{sp}}}",
    "− (N/Nt)(n/tp)": r"-\frac{N}{N_t}\frac{n}{t_p}",
    "Independent check — e^(−2αr d)=R₁R₂, tp=n/(cαr), and Nt=αr/σ₀; no curved mirrors are specified": r"\text{Check:}\quad e^{-2\alpha_r d}=R_1R_2,\quad t_p=\frac{n}{c\alpha_r},\quad N_t=\frac{\alpha_r}{\sigma_0}",
    "Independent check — νq=c(q−Nₘ/2)/Lₒ and adjacent orders differ by νF=c/Lₒ": r"\text{Check:}\quad\nu_q=\frac{c(q-N_m/2)}{L_o},\qquad\nu_F=\frac{c}{L_o}",
    "Independent check — νF=c/(2d), Δν=νF/ℱ, and both reflecting faces point inward": r"\text{Check:}\quad\nu_F=\frac{c}{2d},\qquad\Delta\nu=\frac{\nu_F}{\mathcal{F}}\qquad\text{reflecting faces inward}",
    "Independent check — R₁=R, R₂=−R gives 1/f=2(n−1)/R; a plane surface gives the plano-convex limit": r"\text{Check: }R_1=R,\ R_2=-R\ \Longrightarrow\ \frac{1}{f}=\frac{2(n-1)}{R}\qquad\text{check the plane-surface limit}",
    "Independent check — f=(n₀d₀a²)⁻¹, dimensions, and zero-gradient limit": r"\text{Check:}\quad f=\frac{1}{n_0d_0a^2}\qquad\text{dimensions and zero-gradient limit}",
    "Independent check — 6Ωᶜ/(4π)=ηₑₓₜ; n>√2 makes the six cones disjoint": r"\text{Check:}\quad\frac{6\Omega^c}{4\pi}=\eta_{\mathrm{ext}},\qquad n>\sqrt{2}\ \text{gives disjoint cones}",
    "Independent check — the ray stays in n₁; sin θᶜ=n₂/n₁ and NA²=n₁²−n₂²": r"\text{Check: ray stays in }n_1;\quad\sin\theta^c=\frac{n_2}{n_1},\quad\mathrm{NA}^2=n_1^2-n_2^2",
    "Independent check — the reflecting bowl faces the object; 1/z₁+1/z₂=2/R=1/f": r"\text{Reflecting bowl faces the object;}\quad\frac{1}{z_1}+\frac{1}{z_2}=\frac{2}{R}=\frac{1}{f}",
    "internal interface Adiagonal = 55√2 = 77.78 mm": r"\text{Internal interface:}\quad A_{\mathrm{diagonal}}=55\sqrt{2}=77.78\,\mathrm{mm}",
    "Cf = Adiagonal cos 45° = (55√2) cos 45° = 55 mm — the full diagonal projects back to the cube side": r"C_f=A_{\mathrm{diagonal}}\cos45^\circ=(55\sqrt{2})\cos45^\circ=55\,\mathrm{mm}",
    "fᵦ=|Δν|=2|vᵣ|/λ₀": r"f_b=|\Delta\nu|=\frac{2|v_r|}{\lambda_0}",
}

IGNORED = {
    "Assumes fixed fiber/output optics and rejection of cladding and stray light. Illustration is not a simulated result.",
    "Nodal/principal pair (teal dashed)",
    "Plane/spherical interference",
    "Three/four-level pump power",
    "Shot/Johnson crossover",
    "interface/phase matrices",
    "phase/coupling",
    "tip/tilt: overlap return with launch hole",
    "translate x,y first; tip/tilt second; repeat",
    "margins: 8 mm/fold side; 17.5 mm/perpendicular side",
    "White = transmitting; dashed circles = zone boundaries",
    "Output centres and multiplicities (sum = 36)",
}

SYMBOLS = {
    "α": r"\alpha ", "β": r"\beta ", "γ": r"\gamma ", "δ": r"\delta ",
    "ε": r"\varepsilon ", "η": r"\eta ", "θ": r"\theta ", "κ": r"\kappa ",
    "λ": r"\lambda ", "μ": r"\mu ", "µ": r"\mu ", "ν": r"\nu ",
    "ξ": r"\xi ", "π": r"\pi ", "ρ": r"\rho ", "σ": r"\sigma ",
    "τ": r"\tau ", "φ": r"\phi ", "ϕ": r"\phi ", "χ": r"\chi ",
    "ω": r"\omega ", "ζ": r"\zeta ", "Δ": r"\Delta ", "Ω": r"\Omega ",
    "Λ": r"\Lambda ", "ℱ": r"\mathcal{F}", "ℓ": r"\ell ",
    "−": "-", "–": r"\text{--}", "—": r"\text{---}", "′": "'",
    "″": "''", "∞": r"\infty ", "≈": r"\approx ", "≃": r"\simeq ",
    "≤": r"\le ", "≥": r"\ge ", "≪": r"\ll ", "≫": r"\gg ",
    "∝": r"\propto ", "→": r"\to ", "⇒": r"\Rightarrow ",
    "×": r"\times ", "·": r"\cdot ", "⋅": r"\cdot ",
    "⊕": r"\oplus ", "∩": r"\cap ", "∥": r"\parallel ",
    "⊥": r"\perp ", "∠": r"\angle ", "†": r"^\dagger ",
    "•": r"\quad\bullet\quad ", "…": r"\ldots ", "°": r"^\circ ",
    "½": r"\frac{1}{2}", "Σ": r"\sum ", "∫": r"\int ",
    "±": r"\pm ",
    "↓": r"\downarrow ", "↑": r"\uparrow ",
    "Φ": r"\Phi ", "ℛ": r"\mathcal{R}",
}
SUBSCRIPT = str.maketrans("₀₁₂₃₄₅₆₇₈₉ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓᵧᵦ₍₎", "0123456789aehijklmnoprstuvxyb()")
SUPERSCRIPT = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺⁽⁾ⁿᵀᶜᴮᴸᴼ", "0123456789-+()nTcBLO")
SUBSCRIPT_PATTERN = "[" + re.escape("".join(chr(key) for key in SUBSCRIPT)) + "]+"
SUPERSCRIPT_PATTERN = "[" + re.escape("".join(chr(key) for key in SUPERSCRIPT)) + "]+"
MATH_WORDS = {"NA", "OPL", "BFL", "FFL", "FWHM", "TE", "TM", "IFOV", "AFOV", "HFOV", "VFOV"}
UNITS = {"m", "mm", "cm", "nm", "Hz", "THz", "W", "mW", "kW", "J", "mJ", "K", "V", "F", "s", "eV", "mrad", "pixels", "pulse"}
FUNCTIONS = {"sin", "cos", "tan", "arcsin", "arctan", "exp", "min", "max", "log"}


def text_latex(value: str) -> str:
    escaped = value.replace("\\", r"\textbackslash{}")
    for character in "{}%&#_$":
        escaped = escaped.replace(character, "\\" + character)
    return r"\text{" + escaped + "}"


def latex_for_label(label: str) -> str | None:
    if label in IGNORED:
        return None
    if label in LABELS:
        return LABELS[label]
    replacements = {
        "nₒᵤₜ": r"n_{\mathrm{out}}", "ηₑₓₜ": r"\eta_{\mathrm{ext}}",
        "θs": r"\theta_s", "θP": r"\theta_P", "νq": r"\nu_q",
        "νF": r"\nu_F", "ΔνD": r"\Delta\nu_D", "αr": r"\alpha_r",
        "Vπ": r"V_\pi", "Dν": r"D_\nu", "τp": r"\tau_p",
        "Jδ": r"J_\delta", "Mδ": r"M_\delta",
        "tp": r"t_p", "tsp": r"t_{\mathrm{sp}}", "Nt": r"N_t",
        "Ni": r"N_i", "N0": r"N_0", "N1": r"N_1", "N2": r"N_2",
        "Wi": r"W_i", "nss": r"n_{\mathrm{ss}}", "Aq": r"A_q",
        "TR": r"T_R", "Eout": r"E_{\mathrm{out}}", "ηnet": r"\eta_{\mathrm{net}}",
        "Wf": r"W_f", "Wp": r"W_p", "Cf": r"C_f", "Cp": r"C_p",
        "Adiagonal": r"A_{\mathrm{diagonal}}", "Wfootprint": r"W_{\mathrm{footprint}}",
        "Cfold": r"C_{\mathrm{fold}}", "Avisible": r"A_{\mathrm{visible}}",
    }
    tokens = re.findall(
        "|".join(re.escape(value) for value in sorted(replacements, key=len, reverse=True))
        + r"|[A-Za-z]+\d+|[A-Za-z]+(?:_[A-Za-z0-9]+)?|[0-9]+(?:\.[0-9]+)?|"
        + SUBSCRIPT_PATTERN + "|" + SUPERSCRIPT_PATTERN + r"|\s+|.",
        label,
    )
    result = []
    for token in tokens:
        if token in replacements:
            result.append(replacements[token])
        elif re.fullmatch(r"[A-Za-z]+\d+", token):
            base, number = re.fullmatch(r"([A-Za-z]+)(\d+)", token).groups()
            result.append((r"\mathrm{" + base + "}" if len(base) > 1 else base) + "_{" + number + "}")
        elif token in FUNCTIONS:
            result.append("\\" + token + " ")
        elif token in MATH_WORDS or token in UNITS and len(token) > 1:
            result.append(r"\mathrm{" + token + "}")
        elif re.fullmatch(SUBSCRIPT_PATTERN, token):
            result.append("_{" + token.translate(SUBSCRIPT) + "}")
        elif re.fullmatch(SUPERSCRIPT_PATTERN, token):
            result.append("^{" + token.translate(SUPERSCRIPT) + "}")
        elif token in SYMBOLS:
            result.append(SYMBOLS[token])
        elif re.fullmatch(r"[A-Za-z]+_[A-Za-z0-9]+", token):
            base, subscript = token.split("_", 1)
            result.append(base + "_{" + (r"\mathrm{" + subscript + "}" if len(subscript) > 1 else subscript) + "}")
        elif re.fullmatch(r"[A-Za-z]{2,}", token):
            result.append(text_latex(token))
        elif token.isspace():
            result.append(r"\,")
        elif token in "%&#_$":
            result.append("\\" + token)
        elif token == "^":
            result.append(r"\mathord{\wedge}")
        elif token.isascii():
            result.append(token)
        else:
            raise ValueError(f"Unreviewed character {token!r} in {label!r}")
    return "".join(result)
