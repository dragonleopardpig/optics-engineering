Notation, Models, and Checks
============================

Source conventions
------------------

The core is region 2, with index :math:`n_2` and full thickness
:math:`t` or :math:`t_g`. Region 1 is the cover and region 3 the substrate.
The guide runs along :math:`z`. We write :math:`k_0=2\pi/\lambda_0`,
:math:`N=n_{\mathrm{eff}}=\beta/k_0`, and use the book's time dependence
:math:`e^{i\omega t-i\beta z}`. A guided mode satisfies
:math:`\max(n_1,n_3)<N<n_2`.

The bounce angle :math:`\theta` is measured from the guide plane, so
:math:`\beta=k_0n_2\cos\theta`. The incidence angle from the normal is
:math:`\phi=90^\circ-\theta`. These angles must not be interchanged.
:math:`\Delta n=n_2-n_3` is an index difference; it is not the relative
index difference sometimes also denoted :math:`\Delta`.

Exact slab cutoffs
------------------

Take :math:`n_3\ge n_1`; interchange the cover and substrate labels if
necessary. The transverse and evanescent constants are

.. math::

   h=k_0\sqrt{n_2^2-N^2},\quad
   p=k_0\sqrt{N^2-n_3^2},\quad
   q=k_0\sqrt{N^2-n_1^2}.

For TE modes the branch-safe eigenvalue equation is

.. math::
   :label: integrated-slab-dispersion

   ht=m\pi+\tan^{-1}(p/h)+\tan^{-1}(q/h),\qquad m=0,1,\ldots.

At cutoff :math:`N\to n_3`, giving

.. math::
   :label: integrated-slab-cutoff

   t_{c,m}^{\rm TE}=
   \frac{\lambda_0}{2\pi\sqrt{n_2^2-n_3^2}}
   \left[m\pi+
   \tan^{-1}\sqrt{\frac{n_3^2-n_1^2}{n_2^2-n_3^2}}\right].

For TM replace :math:`p` by :math:`(n_2^2/n_3^2)p` and :math:`q` by
:math:`(n_2^2/n_1^2)q` in the phase equation. At cutoff only the cover
phase remains, so multiply the square root in the arctangent by
:math:`n_2^2/n_1^2`.

Count only orders satisfying :math:`t>t_{c,m}`. An order exactly at
cutoff has an infinite evanescent extent and is not a normalizable bound
mode. Counts here are **per polarization**; a TE and a TM fundamental
are two vector modes.

For a strongly asymmetric, weak-index-step guide,
:math:`q/h\gg1` and :math:`n_2^2-n_3^2\simeq2n_2\Delta n`. Consequently

.. math::
   :label: integrated-asymmetric-approximation

   \Delta n_{c,m}\simeq
   \frac{(2m+1)^2\lambda_0^2}{32n_2t^2}.

This approximation is appropriate to Problems 2.1--2.3. It should not replace
the exact cutoff when the question supplies a general asymmetric structure.

Power, gain, and semiconductor conventions
------------------------------------------

The attenuation coefficient :math:`\alpha` acts on **power**:
:math:`P(z)=P(0)e^{-\alpha z}`. The corresponding field amplitude decays
as :math:`e^{-\alpha z/2}`. Thus loss is
:math:`(10/\ln10)\alpha=4.3429448\alpha` dB per matching length unit.
Natural logarithms appear in propagation and mirror losses; base-10
logarithms convert power ratios to decibels.

For a laser cavity the modal gain is :math:`\Gamma g`, with
:math:`\Gamma\simeq d/D` in the book's simple confinement model. The
intensity reflectivities are :math:`R_1,R_2`, and

.. math::
   :label: integrated-laser-threshold

   \alpha_m=\frac{1}{2L}\ln\frac{1}{R_1R_2},\qquad
   \Gamma g_{\rm th}=\alpha_i+\alpha_m.

Material gain, modal gain, power gain, and amplitude gain are different
quantities. A Fabry--Perot amplifier formula requires a round-trip gain
strictly below one; it cannot be used as a stable unsaturated amplifier
above the lasing threshold.

Useful conversions are :math:`1\,\mu{\rm m}=10^{-4}\,{\rm cm}`,
:math:`1\,{\rm \mathring A}=10^{-10}\,{\rm m}`,
:math:`N[{\rm m}^{-3}]=10^6N[{\rm cm}^{-3}]`,
and

.. math::

   E_\gamma[{\rm eV}]=\frac{1.239841984}{\lambda_0[\mu{\rm m}]},
   \qquad {\cal R}=\eta_q\frac{e\lambda_0}{hc}.

An external differential quantum efficiency specifies a slope above
threshold; it does not, by itself, specify the total output power at a
given current without a threshold current or an intercept.
