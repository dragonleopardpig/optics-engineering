Chapter 22: Nanophotonics
=========================

Source: Hunsperger, sixth edition (2009), Problems 22.1--22.7,
printed page 497.

Problem 22.1 — Photonic-crystal guiding
---------------------------------------

**Working.** A periodic dielectric distribution changes the
allowed electromagnetic Bloch modes. In a photonic bandgap,
certain frequencies cannot propagate in the surrounding
periodic medium. A line defect can create allowed states
inside that gap, confining light to the defect.

**Answer.** Defect-guided propagation can use the contrast
between allowed defect states and forbidden bulk states.

**Check.** Some photonic-crystal structures instead combine
index guiding and directional stop bands. Not every periodic
structure has a complete bandgap for both polarizations.

Problem 22.2 — VCSEL advantages
-------------------------------

**Working.** A short vertical cavity favors a large
longitudinal-mode spacing. A small active volume can lower
threshold current, while the surface-normal output permits
wafer-level testing and two-dimensional arrays. A near-circular
aperture can produce a less asymmetric beam than an
edge-emitting stripe.

**Answer.** Low threshold, array compatibility, accessible
testing, and useful beam geometry are principal advantages.

**Check.** Large-aperture VCSELs can support several transverse
modes. Surface emission alone does not guarantee single-mode
operation or a universally lower divergence.

Problem 22.3 — Rayleigh resolution and lithographic feature size
----------------------------------------------------------------

**Working.** With :math:`D=0.05` m, :math:`f=1` m, and
:math:`\lambda_0=1.55\,\mu{\rm m}`,

.. math::

   \theta_R=1.22\lambda_0/D=3.782\times10^{-5}\,{\rm rad},
   \qquad
   r_R=f\theta_R=37.82\,\mu{\rm m}.

The given approximation yields :math:`{\rm NA}=D/(2f)=0.025`.
With resist factor 0.80,
:math:`W_{\min}=0.80\lambda_0/{\rm NA}=49.6\,\mu{\rm m}`.

**Answer.** (a) Angular Rayleigh separation 37.82 microradians,
or 37.82 micrometres in a focal-plane interpretation.
(b) Lithographic feature size 49.6 micrometres.

**Check.** The Airy diameter is 75.64 micrometres, not the
Rayleigh point separation. A linear object size at an arbitrary
distance would additionally require that distance or magnification.

Problem 22.4 — Electron de Broglie wavelength
---------------------------------------------

**Working.** At :math:`v=2\times10^7` m/s the
nonrelativistic estimate is

.. math::

   \lambda=\frac{h}{m_ev}=3.63695\times10^{-11}\,{\rm m}
   =0.0363695\,{\rm nm}.

**Answer.** Approximately 0.0364 nm.

**Check.** Speed is about 0.0667 times the speed of light.
Using relativistic momentum reduces the wavelength by only
about 0.22 percent, much less than the supplied velocity's precision.

Problem 22.5 — Two anisotropic dry-etch routes
----------------------------------------------

**Working.** In reactive-ion etching, ions accelerated through
a plasma sheath give directional bombardment while reactive
species remove exposed material chemically. Appropriate
sidewall passivation suppresses lateral etching.
In ion-beam or chemically assisted ion-beam etching, a
collimated ion beam provides the directionality; reactive
gas can increase removal rate or selectivity.

**Answer.** RIE and ion-beam/chemically assisted ion-beam
etching are two routes to high-aspect-ratio patterned structures.

**Check.** Mask selectivity, ion damage, redeposition, and
sidewall chemistry still constrain achievable aspect ratio.
Directionality alone is not enough for an arbitrarily deep trench.

Problem 22.6 — What a lattice constant does and does not determine
------------------------------------------------------------------

**Working.** For a square lattice with :math:`a=660` nm,
plane spacing is
:math:`d_{hk}=a/\sqrt{h^2+k^2}`.
A weak-scattering Bragg estimate for incidence normal to
those planes is

.. math::

   \lambda_B\simeq2n_{\rm eff}d_{hk}.

Thus the axial first Bragg estimate is
:math:`1320n_{\rm eff}` nm; the diagonal estimate is
:math:`933.38n_{\rm eff}` nm.

**Answer.** There is no unique blocked wavelength or complete
bandgap interval from lattice constant alone. The dielectric
indices, fill factor, lattice geometry, propagation direction,
and polarization are needed for a Bloch-mode calculation.
For the explicitly assumed :math:`n_{\rm eff}=1` axial
estimate, the Bragg centre would be 1320 nm.

**Check.** A uniform material with an arbitrarily drawn
660 nm grid has no photonic bandgap. A periodic optical
contrast, not just a spacing, is required.

Problem 22.7 — Nanolayer epitaxy
--------------------------------

**Working.** MBE delivers controlled atomic/molecular beams
to a heated crystal under ultrahigh vacuum. MOVPE/MOCVD
reacts controlled vapor-phase precursors at the surface.
For nanolayers, reduce and calibrate growth rate, control
substrate temperature, switch sources/precursors rapidly,
and account for shutter transients, gas residence time,
segregation, and interface roughness.

**Answer.** MBE and MOVPE are the two techniques discussed.
Use layer-resolved process monitoring and calibrated growth
interruptions or pulse times to set nanometre thickness.

**Check.** Measuring average thickness after a long growth
does not establish atomically abrupt interfaces. Strain and
composition control remain necessary alongside timing control.
