Chapter 13: Optical Amplifiers
==============================

Source: Hunsperger, sixth edition (2009), Problems 13.1--13.8,
printed pages 273--274.

Problem 13.1 — Three semiconductor amplifier architectures
----------------------------------------------------------

**Working.** A traveling-wave amplifier suppresses facet reflections
so the signal is amplified predominantly in one transit. A Fabry–Perot
amplifier retains reflecting facets and reinforces resonant signals
through repeated passes, while remaining below threshold.
An injection-locked amplifier is a laser biased above threshold whose
oscillation locks to a suitably matched injected optical signal.

**Answer.** Traveling-wave, Fabry–Perot, and injection-locked amplifiers.
They differ in feedback strength and whether the unseeded device oscillates.

**Check.** All obtain added optical energy from the electrical supply.
An above-threshold injection-locked device is not described by the
same unsaturated linear formula as a below-threshold amplifier.

Problem 13.2 — Select EDFA pump wavelengths
-------------------------------------------

**Working.** Pumping must overlap an erbium absorption band that
feeds the metastable upper laser manifold. The useful 980 nm band
has finite width, so 982 nm can also excite it; the 1480 nm band
directly pumps the upper laser manifold.

**Answer.** 980 nm, 982 nm, and 1480 nm are the intended useful
choices. The listed 855 and 1350 nm values are not the conventional
ground-state pump bands for the illustrated silica EDFA.

**Check.** Pump absorption depends on host, temperature, and the
actual absorption spectrum. A transition band is not a delta function,
so rejecting 982 nm merely because it differs from 980 nm is incorrect.

Problem 13.3 — Signal gain with ASE separated
---------------------------------------------

**Working.** Amplified spontaneous emission is added noise, not
amplified signal. Using 900 mW signal output and 1 mW signal input,

.. math::

   G_{\rm sig}=900,\qquad
   G_{\rm sig,dB}=10\log_{10}(900)=29.5424\,{\rm dB}.

**Answer.** Signal gain is approximately 29.54 dB.

**Check.** Adding the 50 mW ASE would give total output power
950 mW but would overstate useful signal gain. If “stimulated power”
denotes only newly generated power, including the transmitted 1 mW
changes the result slightly to :math:`10\log_{10}(901)`.

Problem 13.4 — Third-harmonic modelocking
-----------------------------------------

**Working.** A linear two-mirror cavity of length 2 m has
:math:`T_{\rm rt}=2n_gL/c`. With negligible dispersion,
:math:`n_g\simeq1.75`, so

.. math::

   f_{\rm rt}=\frac{c}{2(1.75)(2)}=42.8275\,{\rm MHz},\qquad
   f_{\rm lock}=3f_{\rm rt}=128.482\,{\rm MHz}.

**Answer.** Approximately 128.5 MHz.

**Check.** A ring cavity would have a different round-trip length.
The optical carrier wavelength does not set the repetition rate
once optical path length is specified.

Problem 13.5 — Amplifier wavelength ranges
------------------------------------------

**Working.** Gain bandwidth depends on the active transition or
Raman shift, not just the presence of a waveguide.

.. list-table:: Ranges in the context of the sixth edition
   :header-rows: 1

   * - Amplifier
     - Interpretation
   * - SOA
     - Different semiconductor compositions span roughly 0.8--1.6 micrometres;
       one device covers only its material gain band.
   * - EDFA
     - Roughly 1.52--1.60 micrometres across C/L-band implementations;
       strongest conventional gain is near 1.55 micrometres.
   * - Raman
     - Pump-selectable Stokes gain, with silica's main peak near
       :math:`\nu_s=\nu_p-13.2\,{\rm THz}`.
   * - TDFA
     - The book discusses S-band systems around 1.48--1.52 micrometres
       and a pumping scheme with a broader 1.43--1.50 micrometre response.

**Answer.** Give a range together with host, pumping scheme, and
device family; Raman amplification has no single universal absolute band.

**Check.** Stokes Raman gain is at lower frequency and longer
wavelength than the pump. A 1500 nm pump cannot generate a
1480 nm Stokes signal; that numerical passage in the chapter is inconsistent.

Problem 13.6 — Check the proposed Fabry–Perot amplifier first
-------------------------------------------------------------

**Working.** The net single-pass power gain is

.. math::

   G_s=e^{(\Gamma g-\alpha)L}
   =e^{[(0.9)(50)-4](0.035)}=4.19965.

For equal facet reflectivity 0.33, the round-trip power factor is
:math:`R^2G_s^2`, and :math:`RG_s=1.38588>1`.

**Answer.** (a) The specified unsaturated device is already above
lasing threshold. There is no stable small-signal Fabry–Perot amplifier
gain at that operating point without saturation or a changed bias.
(b) With negligible facet reflection and the assumed same material
gain, the traveling-wave gain is 4.19965, or about 6.23 dB.

**Check.** Algebraically evaluating
:math:`(1-R)^2G_s/(1-RG_s)^2` above threshold produces a number
outside the formula's physical domain. Carrier density may also change
when feedback is removed at fixed injection current.

Problem 13.7 — Stimulated photon generation rate
------------------------------------------------

**Working.** Divide stimulated optical power by one photon's energy:

.. math::

   \dot N_\gamma=\frac{P\lambda_0}{hc}
   =\frac{(0.850)(1536\times10^{-9})}{hc}
   =6.57254\times10^{18}\,{\rm s}^{-1}.

**Answer.** Approximately :math:`6.57\times10^{18}` photons/s.

**Check.** Use watts rather than milliwatts. This is a generation
rate, not the stored number of photons in the amplifier.

Problem 13.8 — A second above-threshold amplifier specification
---------------------------------------------------------------

**Working.** With :math:`G_s=15` and :math:`R=0.65`,
the round-trip power multiplier is

.. math::

   R^2G_s^2=(0.65)^2(15)^2=95.0625.

**Answer.** The unsaturated specification is far above threshold,
so it does not define a stable linear Fabry–Perot amplifier.
Stable operation would require :math:`G_s<1/R=1.53846`.

**Check.** The squared denominator in the formal resonant-gain
expression does not make the above-threshold solution physical.
Gain clamping or injection-locking would require additional information.
