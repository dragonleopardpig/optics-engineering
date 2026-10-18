Chapter 11: Light Emission in Semiconductors
============================================

Source: Hunsperger, sixth edition (2009), Problems 11.1--11.10,
printed pages 238--239.

Problem 11.1 — Linewidth, inversion, and divergence
---------------------------------------------------

**Working.** An LED emits spontaneously across a distribution of occupied
electron and hole energies; it has no strong cavity selection.
A laser preferentially amplifies resonant modes, narrowing the spectrum.
Laser operation needs population inversion at the photon energy and
modal gain sufficient to overcome the complete cavity loss.

The small laser aperture still diffracts: roughly
:math:`\theta_{\rm div}\sim\lambda_0/w`. Its uncollimated far
field can span tens of degrees, with different divergences along the
thin and wide axes. A lens increases beam diameter and reduces divergence.

**Answer.** Spectral selection and stimulated emission produce narrow
laser lines, but do not eliminate diffraction from a micrometre aperture.

**Check.** The textbook linewidths are representative, not universal
limits. A single laser can have multiple narrow longitudinal lines.

Problem 11.2 — Einstein absorption and stimulated-emission coefficients
-----------------------------------------------------------------------

**Working.** Divide the supplied equilibrium balance by photon density:

.. math::

   B_{12}N_1=B_{21}N_2+\frac{A_{21}N_2}{\rho}.

As :math:`\rho\to\infty`, this establishes
:math:`B_{12}N_1=B_{21}N_2`. For a nondegenerate two-level
system in the high-temperature equilibrium limit,
:math:`N_1/N_2\to1`, giving :math:`B_{12}=B_{21}`.

**Answer.** The requested equality follows with the implicit equal-degeneracy,
equal-limiting-population assumption. More generally
:math:`g_1B_{12}=g_2B_{21}`.

**Check.** The supplied balance equation and large photon density
alone do not prove equal coefficients for arbitrary populations.
The population/degeneracy assumption must be made explicit.

Problem 11.3 — Photon wavelength from momentum conservation
-----------------------------------------------------------

**Working.** For the collinear direct transition,
:math:`k_\gamma=k_f-k_i=10^5\,{\rm cm}^{-1}`.
Wavevector magnitude is :math:`2\pi/\lambda`, so

.. math::

   \lambda_{\rm medium}=\frac{2\pi}{10^5}\,{\rm cm}
   =0.628319\,\mu{\rm m}.

**Answer.** The photon wavelength in the material is 0.6283 micrometres.
Its vacuum wavelength is :math:`n(\omega)` times this value.

**Check.** No refractive index is supplied, so a unique vacuum
wavelength does not follow. Replacing :math:`2\pi/k` by
:math:`1/k` confuses angular wavevector and spectroscopic wavenumber.

Problem 11.4 — Efficiency of a laser relative to an LED
-------------------------------------------------------

**Working.** Above threshold, stimulated recombination directs a large
fraction of incremental injected carriers into selected optical modes.
An LED distributes spontaneous emission across many directions and
frequencies, and useful extraction can be limited by total internal
reflection and packaging.

**Answer.** A laser can convert incremental current efficiently into
a useful directed coherent beam.

**Check.** This is not a universal statement about total wall-plug
efficiency. The laser pays a threshold-current overhead, and a well-designed
LED can be more efficient at low required output.

Problem 11.5 — Spectra below, at, and above threshold
-----------------------------------------------------

**Working.** Below threshold draw a broad spontaneous-emission envelope.
Near threshold, cavity resonances emerge on that envelope. Above
threshold, draw narrow, stronger resonant lines and a relatively weak
spontaneous background.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/laser_spectra.svg
   :alt: Broad below-threshold spectrum, emerging cavity lines near threshold, and narrow dominant lines above threshold.
   :width: 100%

   Illustrative spectra; widths and amplitudes are not measurement data.

**Answer.** The change is both spectral narrowing and redistribution
of power into oscillating modes.

**Check.** A Fabry–Perot laser above threshold need not be
single-longitudinal-mode. Do not replace every above-threshold spectrum
by one line automatically.

Problem 11.6 — Quasi-Fermi levels and the gain band
---------------------------------------------------

**Working.** Forward injection creates separate electron and hole
quasi-Fermi levels, :math:`E_{Fn}` and :math:`E_{Fp}`.
For net interband stimulated emission at photon energy :math:`h\nu`,
the idealized inversion criterion is

.. math::

   E_g<h\nu<E_{Fn}-E_{Fp}.

Draw the conduction and valence edges, reduced junction barrier,
and separate quasi-Fermi levels in the injected active region.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/laser_bands.svg
   :alt: Forward-injected band edges and separate quasi-Fermi levels, compared with double-heterostructure carrier barriers.
   :width: 100%

   Schematic electron-energy profiles.

**Answer.** The longest-wavelength ideal gain edge corresponds to
:math:`E_g`; the shortest corresponds to quasi-Fermi separation.

**Check.** Finite temperature, band filling, loss, and cavity resonances
modify the actual lasing spectrum. The inequality is a gain window,
not a prediction that every frequency in it oscillates.

Problem 11.7 — High optical power density in semiconductors
-----------------------------------------------------------

**Working.** A solid contains a very high density of available electronic
states compared with a dilute gas. Injection concentrates carriers in
a small active region, and direct transitions can supply large gain
over a short distance. Optical and carrier confinement further shrink
the useful active volume.

**Answer.** High carrier density and strong confined gain permit
large generated power per active volume.

**Check.** Power density is limited by heat extraction, gain saturation,
and damage. A small volume does not imply an unlimited total output power.

Problem 11.8 — Why the Fermi levels are only quasi-Fermi levels
---------------------------------------------------------------

**Working.** Pumping maintains a nonequilibrium electron-hole population.
Fast intraband scattering can approximately thermalize each carrier
population separately, allowing one Fermi–Dirac distribution for
electrons and another for holes. Interband recombination has not
returned them to a common chemical potential.

**Answer.** Two quasi-Fermi levels describe internally equilibrated
subsystems that are not in mutual equilibrium.

**Check.** At thermal equilibrium the two levels coincide. A single
equilibrium Fermi level cannot describe sustained population inversion.

Problem 11.9 — Compare laser-diode and LED light
------------------------------------------------

**Working.** An LED produces predominantly spontaneous emission with
broad spectral and angular distributions and low mutual coherence
between emission events. A laser has feedback-selected stimulated
emission, giving narrow lines, stronger coherence, and a useful
directional output. Its finite aperture still produces an asymmetric,
divergent beam.

**Answer.** Compare spectrum, coherence, directionality, and threshold
behavior; these distinguish the mechanisms more clearly than brightness alone.

**Check.** Neither perfect collimation nor perfect monochromaticity
is a necessary laser property. Both devices require suitable
collection optics for a specified application.

Problem 11.10 — Photon energy including carrier excess energies
---------------------------------------------------------------

**Working.** The electron is 20 meV above the conduction edge;
the final valence state is 35 meV below its edge. Therefore

.. math::

   E_\gamma=E_g+0.020+0.035\,{\rm eV},\qquad
   \lambda_0=\frac{1.239841984}{E_g+0.055}\,\mu{\rm m}.

**Answer.** With a stated room-temperature GaAs approximation
:math:`E_g=1.43` eV, :math:`\lambda_0\simeq0.83491\,\mu{\rm m}`.

**Check.** Both excess energies add. Temperature is not given in
the problem; using 1.42 eV instead produces 0.84057 micrometres.
The symbolic expression exposes that material-data dependence.
