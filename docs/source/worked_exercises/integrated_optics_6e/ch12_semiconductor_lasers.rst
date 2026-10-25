Chapter 12: Semiconductor Lasers
================================

Source: Hunsperger, sixth edition (2009), Problems 12.1--12.13,
printed pages 255--257.

Injection model used in this chapter
------------------------------------

Combining the book's gain-current relation with modal threshold gives

.. math::
   :label: integrated-current-threshold

   J_{\rm th}=A(\alpha_i+\alpha_m),\qquad
   A=\frac{8\pi en^2\Delta\nu D}{\eta_q\lambda_0^2}.

Use centimetres for :math:`D,\lambda_0,L` when current density is
in A/cm2 and attenuation is in inverse centimetres.
Above threshold, a linear differential-efficiency model uses
:math:`I-I_{\rm th}`. The book's Eq. (12.20) instead approximates
generated power as proportional to total current. The distinction is
important in the first exercise.

Problem 12.1 — Pulsed rangefinder laser
---------------------------------------

**Working.** Convert the half-power wavelengths into frequency width:

.. math::

   \Delta\nu=c\left(\frac1{0.88\,\mu{\rm m}}-
   \frac1{0.92\,\mu{\rm m}}\right)=1.48119\times10^{13}\,{\rm Hz}.

Set :math:`B=\ln(1/0.4)=0.916291`,
:math:`Q=\eta_qh\nu/e=0.964322\,{\rm W/A}`,
:math:`W=0.03` cm, :math:`\alpha_i=30\,{\rm cm}^{-1}`,
and total two-face output :math:`P=20` W.
The printed output model is

.. math::

   P=QJWL\frac{B}{\alpha_iL+B},\qquad
   L=\frac{PB}{QJWB-P\alpha_i}.

**Answer.** Following that model, :math:`L=0.0938635` cm,
or 938.6 micrometres. With field thickness :math:`D=10\,\mu{\rm m}`,
:eq:`integrated-current-threshold` then gives
:math:`J_{\rm th}=4554.84\,{\rm A/cm^2}`.

**Check.** Both end faces must be counted, even though only one
is used. If the output model is corrected to the usual
:math:`P=Q(I-I_{\rm th})B/(\alpha_iL+B)`, the required
length becomes about 2.027 mm and its threshold about
3954 A/cm2. These are different model assumptions, not rounding errors.

Problem 12.2 — Heat-limited pulse repetition rate
-------------------------------------------------

**Working.** With the printed-model length from 12.1,
:math:`I_{\rm pk}=JWL=84.477` A. Neglecting series-resistance
loss does not determine the junction voltage. For junction voltage
:math:`V_j`, heat per pulse is

.. math::

   E_{\rm heat}=(V_jI_{\rm pk}-20\,{\rm W})(100\,{\rm ns}),\qquad
   f_{\max}=\frac{1\,{\rm W}}{E_{\rm heat}}.

**Answer.** With the additional photon-voltage approximation
:math:`V_j=h\nu/e=1.37760` V, :math:`f_{\max}\simeq103.76` kHz.
Otherwise retain the displayed voltage-dependent answer.

**Check.** Subtract the optical output from both faces, since both
leave the chip. Using only the useful 10 W beam overestimates
device heating. Thermal pulse limits can impose further restrictions.

Problem 12.3 — Minimum unambiguous pulse separation in range
------------------------------------------------------------

**Working.** A colocated receiver sees a round-trip delay
:math:`2R/c`. Require it to be at least the 100 ns transmitted
pulse duration:

.. math::

   R_{\min}=\frac{c\tau}{2}
   =\frac{(299792458)(100\times10^{-9})}{2}
   =14.9896\,{\rm m}.

**Answer.** Approximately 15.0 m, before adding detector recovery
time or other timing margins.

**Check.** Pulse repetition rate limits maximum unambiguous range,
whereas pulse duration controls this minimum nonoverlap range.

Problem 12.4 — Stimulated emission, threshold, and confinement
--------------------------------------------------------------

**Working.** A pumped gain medium can amplify light through stimulated
emission without mirrors; an injected coherent seed can remain coherent.
Without a feedback oscillator, amplified spontaneous emission is not
automatically a single coherent laser mode.

Threshold occurs when round-trip gain compensates every round-trip loss.
Confinement raises the fraction of field sampling the inverted carriers,
reducing material gain and current needed for threshold. The large
semiconductor divergence arises from its tiny emitting aperture,
not from the absence of stimulated emission.

**Answer.** Feedback is required for ordinary laser oscillation, while
stimulated amplification itself does not require a resonator.

**Check.** “No mirrors” does not exclude distributed or other feedback.
Distinguish gain, coherence of a seed, and self-sustained oscillation.

Problem 12.5 — Gap and approximate drive current
------------------------------------------------

**Working.** For 1.2 micrometres,
:math:`E_g\simeq hc/\lambda_0=1.03320` eV. If the quoted 15
percent is an overall emitted-photon-per-injected-electron efficiency,

.. math::

   I=\frac{Pe}{\eta_{\rm ext}h\nu}
   =\frac{0.020}{0.15(1.03320)}=0.129049\,{\rm A}.

**Answer.** Gap about 1.033 eV and estimated current 129 mA.

**Check.** If 15 percent denotes a differential efficiency instead,
this calculation gives excess current above threshold; add
:math:`I_{\rm th}` to obtain total current.

Problem 12.6 — Double cavity length with fixed mirror reflectivity
------------------------------------------------------------------

**Working.** Internal loss is :math:`5+0.5=5.5\,{\rm cm}^{-1}`.
With identical mirror reflectivity 0.65, the original mirror loss is
:math:`\alpha_m=\ln(1/0.65)/L`. Doubling length halves only
that contribution.

.. math::

   \frac{J_{\rm th}(2L)}{J_{\rm th}(L)}
   =\frac{5.5+\ln(1/0.65)/(2L)}
          {5.5+\ln(1/0.65)/L}.

**Answer.** The ratio lies between one half and one. No single
number follows without the original length.

**Check.** The ratio approaches one half for mirror-dominated loss
and one for internal-loss-dominated operation.

Problem 12.7 — One perfectly reflecting end
-------------------------------------------

**Working.** Apply round-trip intensity balance:

.. math::

   R_0\exp[2(\Gamma g-\alpha_i)L]=1,\qquad
   g_{\rm th}=\frac1{\Gamma}\left[
   \alpha_i+\frac1{2L}\ln\frac1{R_0}\right].

With :math:`J=Kg` and :math:`\Gamma=d/D`,

.. math::

   J_{\rm th}=K\frac{D}{d}
   \left[\alpha_i+\frac1{2L}\ln\frac1{R_0}\right].

**Answer.** The output-mirror logarithm carries a factor of one half
because only one end transmits.

**Check.** Setting both mirrors equal to :math:`R_0` doubles
the logarithmic mirror contribution at fixed length.

Problem 12.8 — Piecewise optical power versus current
-----------------------------------------------------

**Working.** Interpret the specified below/above-threshold efficiencies
as slopes, keeping power continuous at 12 A. At 0.85 micrometres,
:math:`h\nu/e=1.45864` V. Then

.. math::

   P(I)=
   \begin{cases}
   0.01(1.45864)I,&I\le12\,{\rm A},\\
   0.175037+0.10(1.45864)(I-12),&I>12\,{\rm A}.
   \end{cases}

**Answer.** Threshold output is 0.1750 W; output at 18 A is
1.0502 W. Plot these two straight segments through 20 A.

**Check.** Assigning :math:`P=0.1(h\nu/e)I` immediately above
threshold creates an unphysical discontinuity. An overall efficiency
and a differential slope are not interchangeable.

Problem 12.9 — Longitudinal spacing with dispersion
---------------------------------------------------

**Working.** Differentiate :math:`2n(\lambda)L=m\lambda`:

.. math::

   \Delta\lambda\simeq\frac{\lambda^2}{2L n_g},\qquad
   n_g=n-\lambda\,dn/d\lambda.

With the quoted positive dispersion interpreted literally as
:math:`dn/d\lambda=+0.5\,\mu{\rm m}^{-1}`,
:math:`n_g=3.15` and :math:`\Delta\lambda=0.428571` nm.

**Answer.** 0.429 nm for that signed derivative. If the quoted
0.5 is the magnitude of a negative derivative, :math:`n_g=4.05`
and spacing is 0.333333 nm.

**Check.** A positive number called “dispersion” without a derivative
sign convention is ambiguous. Both interpretations are exposed here.

Problem 12.10 — Differential quantum and power efficiencies
-----------------------------------------------------------

**Working.** Each incremental electron supplies electrical energy
:math:`eV` and creates :math:`\eta_d` output photons on average:

.. math::

   \eta_{\rm power,diff}=\eta_d\frac{h\nu}{eV}
   =0.30\frac{1.37760}{2.5}=0.165312.

**Answer.** Differential power efficiency is 16.53 percent.

**Check.** The total wall-plug efficiency also includes threshold
overhead. With negligible threshold output and constant voltage it is
approximately this result times :math:`1-I_{\rm th}/I`.
The supplied differential efficiency does not establish an exact
overall efficiency without operating current.

Problem 12.11 — Minimum equal-mirror reflectivity
-------------------------------------------------

**Working.** With unit confinement,
:math:`g-\alpha_i=70-5=65\,{\rm cm}^{-1}`.
Round-trip threshold gives :math:`R^2e^{2(65)(0.03)}=1`.

.. math::

   R_{\min}=e^{-(65)(0.03)}=0.142274.

**Answer.** Approximately 14.23 percent intensity reflectivity
at each end; lower reflectivity would exceed the specified available gain.

**Check.** Length is 0.03 cm, not 300 cm. The equal-mirror result
contains one factor of :math:`L` in its final exponent.

Problem 12.12 — Double length at constant threshold density
-----------------------------------------------------------

**Working.** Internal loss and current-to-gain relation stay fixed,
so equal threshold density requires equal mirror loss:

.. math::

   \frac1{2L}\ln\frac1{R'}=\frac1L\ln\frac1R
   \quad\Longrightarrow\quad R'=R^2.

For unchanged width, injection area :math:`LW` doubles.

**Answer.** (a) Each new mirror has reflectivity :math:`R^2`.
(b) Threshold current doubles even though threshold current density does not.

**Check.** Lower reflectivity compensates the longer cavity.
Current and current density must not be confused.

Problem 12.13 — Tunnel injection after halving the insulator thickness
----------------------------------------------------------------------

**Working.** The book uses
:math:`J(E)=J_0(E/E_0)^2e^{-E_0/E}`.
At fixed applied voltage, halving thickness doubles the field:

.. math::

   \frac{J(2E)}{J(E)}=4\exp[E_0/(2E)].

**Answer.** With :math:`E=4\times10^4\,{\rm V/m}`, the factor is
:math:`4\exp[E_0/(8\times10^4\,{\rm V/m})]`.
The measured 1500 A/cm2 alone does not determine :math:`E_0`
or a numerical increase. If the field rather than voltage is held fixed,
this field-only model predicts no change.

**Check.** The missing barrier/effective-mass information cannot
be recovered from one measurement containing two unknown constants.
