Chapter 17: Integrated Optical Detectors
========================================

Source: Hunsperger, sixth edition (2009), Problems 17.1--17.11,
printed pages 368--371.

Problem 17.1 — Choose a detector gap
------------------------------------

**Working.** A 0.9 micrometre photon has energy 1.37760 eV.
Direct interband absorption therefore excludes the 2 eV material.
Both 0.5 and 1 eV gaps can absorb, but the larger qualifying gap
generally suppresses thermally generated dark carriers.

**Answer.** The 1 eV material is the intended compromise when
the other stated material properties are equivalent.

**Check.** Bandgap alone does not determine detector noise, absorption
length, or carrier transport. The conclusion uses the question's
equal-quality assumptions.

Problem 17.2 — Reject short-wavelength background
-------------------------------------------------

**Working.** Require
:math:`e^{-(1000\,{\rm cm}^{-1})t}=10^{-4}`, so

.. math::

   t=\ln(10^4)/1000=0.00921034\,{\rm cm}=92.1034\,\mu{\rm m}.

At the signal wavelength, transmission is
:math:`T_s=e^{-0.2t}=0.9981596`.

**Answer.** A roughly 92.1 micrometre filter suppresses the
background by 10,000 while transmitting 99.816 percent of the signal.

**Check.** Signal attenuation factor can mean either
:math:`T_s=0.99816` or input/output ratio
:math:`1/T_s=1.00184`; specify which is quoted.

Problem 17.3 — Minimum irradiance for a photocurrent
----------------------------------------------------

**Working.** With :math:`\eta_q=0.8` at 0.9 micrometres,
:math:`{\cal R}=\eta_qe\lambda_0/(hc)=0.5807` A/W.
Required incident power is :math:`P=I/{\cal R}=1.7220\,\mu{\rm W}`.
The sensitive area is :math:`10\,{\rm mm^2}=10^{-5}\,{\rm m^2}`.

**Answer.** Required peak irradiance is
:math:`0.17220\,{\rm W/m^2}`, or
:math:`17.220\,\mu{\rm W/cm^2}`.

**Check.** This assumes the stated quantum efficiency refers to
incident photons. If it is only internal yield, include reflection
and incomplete absorption separately.

Problem 17.4 — Material selection and silicon photocurrent
----------------------------------------------------------

**Working.** Approximate the GaAs laser photon energy by the
listed GaAs gap, 1.4 eV. Si, GaAs, GaSb, and InAs have
gaps no larger than that value; GaP does not. Adding Sb or In
to GaAs can reduce the gap, whereas adding P generally raises
it in the relevant composition range.

For 10 mW incident on 1 cm2 and :math:`\eta_q=0.8`,

.. math::

   I=\eta_q\frac{eP}{E_\gamma}
   \simeq0.8\frac{0.010}{1.4}=5.7143\,{\rm mA}.

**Answer.** GaAsSb and InGaAs can provide the needed lower gap;
GaAsP generally cannot except at the GaAs endpoint or with sufficient
photon excess energy. The illustrative silicon current is 5.71 mA.

**Check.** Gap equality is only a threshold condition, not a guarantee
of strong absorption. If an exact wavelength is specified, use it
instead of equating photon energy to the approximate gap.

Problem 17.5 — Photon threshold and pair generation
---------------------------------------------------

**Working.** At 0.600 micrometres,
:math:`E_\gamma=2.06640` eV, the largest qualifying gap.
Incident power is :math:`P=(20)(5\times10^{-6})=10^{-4}` W.
For unit external quantum efficiency,

.. math::

   \dot N=\frac{P\lambda_0}{hc}
   =3.02047\times10^{14}\ {\rm pairs/s}.

**Answer.** (a) Maximum gap 2.0664 eV.
(b) :math:`3.02047\times10^{14}` pairs/s.
(c) Halving intensity halves the rate.
(d) Halving wavelength at fixed intensity also halves the rate.

**Check.** Shorter-wavelength photons carry more energy, so fixed
optical power means fewer photons, not more.

Problem 17.6 — Field-assisted absorption length
-----------------------------------------------

**Working.** Average depletion field is
:math:`E=40.5/(3\times10^{-6})=1.35\times10^7` V/m.
The book's Franz–Keldysh energy-scale estimate gives

.. math::

   \Delta E=\frac32(m^*)^{-1/3}(e\hbar E)^{2/3}
   \simeq0.08877\,{\rm eV}

for :math:`m^*=0.067m_0`.
Fig. 17.19 gives about :math:`\alpha=10^4\,{\rm cm}^{-1}`
at 0.9 micrometres for this field. Require
:math:`1-e^{-\alpha L}=0.99`.

**Answer.** The characteristic absorption-edge shift is about
88.8 meV; :math:`L=\ln100/\alpha\simeq4.605\,\mu{\rm m}`
for full optical overlap.

**Check.** The shift is a field-assisted absorption scale, not a
rigid change to the crystal's true gap. With confinement factor
:math:`\Gamma<1`, replace :math:`\alpha` by :math:`\Gamma\alpha`.

Problem 17.7 — Audit all optoisolator combinations
--------------------------------------------------

**Working: wavelengths and transparency.** Laser (a) has
:math:`\lambda_a=2(3.6)(0.340)/3=0.816\,\mu{\rm m}`.
Lasers (b) and (c) emit at 0.9 micrometres. At 0.816 micrometres
the Fig. 4.8 curves show strong absorption in both candidate guide
cores, eliminating the long guide routes for (a). Its source efficiency
and threshold are also not specified well enough for an independent
current-transfer calculation.

**Working: electrical feasibility.** For (b) and (c),
:math:`\alpha_m=\ln(1/0.4)/0.0935=9.800\,{\rm cm}^{-1}`.
Using the supplied spontaneous width and modal thicknesses in
:eq:`integrated-current-threshold` gives

.. math::

   I_{{\rm th},b}\simeq12.79\,{\rm A}>5\,{\rm A},\qquad
   I_{{\rm th},c}\simeq0.6362\,{\rm A}.

Thus (b) cannot operate as the assumed laser at the available drive.
For (c), the one-facet photon efficiency at 5 A is approximately

.. math::

   \eta_{c,1}=\frac{\eta_q}{2}
   \frac{\alpha_m}{\alpha_i+\alpha_m}
   \left(1-\frac{I_{\rm th}}{I}\right)
   =0.15119.

**Working: current-transfer ratios.** For a guide with transmission
:math:`T` and a detector absorbing fraction :math:`A_D` with
internal yield one and avalanche factor :math:`M`,

.. math::

   {\rm CTR}=I_{\rm out}/I_{\rm in}=\eta_{c,1}T A_D M.

For detector (f), using the zero-field 0.9 micrometre absorption
:math:`25\,{\rm cm}^{-1}` from Fig. 17.19 and length 0.01 cm gives
:math:`A_f=1-e^{-0.25}=0.22120`.
With :math:`M_f=2`, even perfect guide transmission gives
:math:`{\rm CTR}_{c,f}\le0.06689<0.1`.
If its avalanche field also changes absorption, that new absorption
must instead be supplied; multiplication alone does not specify it.

For detector (g), strong field makes :math:`A_g\simeq1`, hence
:math:`{\rm CTR}_{c,g}\simeq0.15119T`.
It passes only if

.. math::

   T\ge0.66142,\qquad
   \alpha_d\le\frac{-\ln0.66142}{0.5}=0.827\,{\rm cm}^{-1},
   \quad
   \alpha_e\le\frac{-\ln0.66142}{0.2}=2.07\,{\rm cm}^{-1}.

**Answer.** These inequalities are the explicit acceptance test for
the remaining (c,d,g) and (c,e,g) routes. For illustrative book-graph
readings :math:`\alpha_d\simeq2` and
:math:`\alpha_e\simeq25\,{\rm cm}^{-1}`, their one-facet ratios
are only about 0.0556 and 0.00102, so neither meets 0.1.
The (c,*,f) routes fail with the stated zero-field absorption model;
(b,*,*) fails the drive limit; the (a,*,*) routes are strongly absorbed.

**Check.** This exercise is sensitive to graph readings, field-modified
detector absorption, and one-face versus two-face collection.
The book's Chapter 12 power expression counts **both** faces.
Allocating that total to the single waveguide doubles CTR and can
make (c,d,g) appear acceptable. If both faces really are collected,
state that additional optical arrangement explicitly and double the
one-face results. Unit internal yield does not mean every incident
photon is absorbed.

Problem 17.8 — Avalanche photocurrent from an irradiance
--------------------------------------------------------

**Working.** Incident power is
:math:`(10^{-3}\,{\rm W/cm^2})(10^{-4}\,{\rm cm^2})=10^{-7}` W.
With 0.85 quantum efficiency and avalanche factor 1000,

.. math::

   I=M\eta_q\frac{e\lambda_0P}{hc}
   =89.1243\,\mu{\rm A}.

**Answer.** Approximately 89.1 microamperes.

**Check.** Area is required because the supplied optical datum is
irradiance. Multiplication affects carriers, not the photon energy.

Problem 17.9 — Infer avalanche factor and gap
---------------------------------------------

**Working.** At 1.3 micrometres and quantum efficiency 0.8,
the unmultiplied current for 1 microwatt is
:math:`I_0={\cal R}P=0.83884\,\mu{\rm A}`.
Therefore :math:`M=20/I_0=23.8431`.
The 1.7 micrometre cutoff estimates
:math:`E_g=1.239841984/1.7=0.729319` eV.

**Answer.** Avalanche factor about 23.84; absorber gap about 0.729 eV.

**Check.** Use the cutoff wavelength for the gap and the operating
wavelength for responsivity. They serve different purposes.

Problem 17.10 — p-i-n and avalanche advantages
----------------------------------------------

**Working.** An intrinsic layer gives a p-i-n detector a broad
depleted absorption region with a controlled electric field and
reduced junction capacitance. It can combine useful absorption with
rapid drift collection. An APD adds impact-ionization multiplication
before external electrical amplification.

**Answer.** The p-i-n architecture improves the absorption,
capacitance, and speed tradeoff; the APD provides internal current gain.

**Check.** APD multiplication also adds excess noise and bias
sensitivity. Larger internal current is not automatically better
signal-to-noise in every receiver.

Problem 17.11 — Silicon p-i-n photocurrent
------------------------------------------

**Working.**

.. math::

   I=\eta_q\frac{e\lambda_0P}{hc}
   =(0.55)\frac{e(1.0\times10^{-6})(100\times10^{-9})}{hc}
   =4.43605\times10^{-8}\,{\rm A}.

**Answer.** Approximately 44.36 nA.

**Check.** Negligible dark current means no dark-current subtraction
is needed, but shot noise and amplifier noise have not thereby vanished.
