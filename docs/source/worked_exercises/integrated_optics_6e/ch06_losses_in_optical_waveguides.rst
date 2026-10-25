Chapter 6: Losses in Optical Waveguides
=======================================

Source: Hunsperger, sixth edition (2009), Problems 6.1--6.11,
printed pages 125--127. Attenuation coefficients here act on power.

Problem 6.1 — Local meaning of attenuation
------------------------------------------

**Working.** Differentiate the assumed exponential:

.. math::

   \frac{dP}{dz}=-\alpha P_0e^{-\alpha z}=-\alpha P(z)
   \quad\Longrightarrow\quad
   \alpha=\frac{-dP/dz}{P(z)}.

**Answer.** Attenuation is the positive power lost per unit distance
divided by the power being transmitted at that position.

**Check.** The dimensions are inverse length. This is a local ratio,
not the cumulative power lost since the input divided by current power.

Problem 6.2 — Convert exponential loss to decibels
--------------------------------------------------

**Working.** Over a distance :math:`z`,

.. math::

   L_{\rm dB}=10\log_{10}\frac{P(0)}{P(z)}
   =10\log_{10}(e^{\alpha z})
   =\frac{10}{\ln10}\alpha z.

**Answer.** Loss per unit length is :math:`4.3429448\alpha`,
or :math:`4.3\alpha` at the precision used in the question.

**Check.** :math:`\alpha=1\,{\rm cm}^{-1}` leaves
:math:`e^{-1}` of the input after 1 cm, equivalent to 4.343 dB.
The factor 8.686 applies to an amplitude attenuation coefficient instead.

Problem 6.3 — Loss of the intermediate-radius bend
--------------------------------------------------

**Data.** The straight BC section is 0.5 cm; the DE, AB, and CD
quarter-circle radii are 0.1, 0.2, and 0.3 cm.

**Working.** The straight loss is :math:`s=1.00/0.5=2` dB/cm.
Divide each measured bend loss by :math:`\pi R/2` and subtract
:math:`s` to obtain radiation loss per length:

.. math::

   r(0.1)=\frac{1.01}{0.05\pi}-2=4.4293,\qquad
   r(0.3)=\frac{1.22}{0.15\pi}-2=0.5890.

Under the fixed-mode exponential-radius model of Eq. (6.40),
:math:`r(R)=Ae^{-BR}`. At the intermediate radius,
:math:`r(0.2)=\sqrt{r(0.1)r(0.3)}`.

**Answer.**
:math:`L_{AB}=[2+r(0.2)](0.1\pi)=1.13575` dB.

**Check.** This is conditional on the book's exponential bend-loss
approximation. Two measured bend radii alone cannot determine an
arbitrary radiation-loss function.

Problem 6.4 — Why tight bends radiate more
------------------------------------------

**Working.** Parts of a mode on the outer side of a bend must cover
a longer path per unit angle than the field near its centre. Beyond
a critical outer radius, the exterior field can no longer remain phase
locked to the guided mode. Its evanescent barrier is effectively reduced,
allowing radiation to escape.

**Answer.** Reducing bend radius moves the radiation region closer
to the core, where more of the modal tail resides, increasing loss.

**Check.** A more tightly confined mode usually tolerates smaller
radii than a weakly confined mode. Bending loss is distinct from
absorption heating and roughness scattering.

Problem 6.5 — Minimum radius under a loss limit
-----------------------------------------------

**Working.** Subtract the straight-guide background:
:math:`\alpha_r(0.5)=1.1\,{\rm cm}^{-1}` and
:math:`\alpha_r(0.3)=26.0\,{\rm cm}^{-1}`, with radii in mm.
Fit :math:`\alpha_r=Ae^{-BR}`:

.. math::

   B=\frac{\ln(26/1.1)}{0.2\,{\rm mm}},\qquad
   R_{\rm limit}=0.5-\frac{\ln(2.7/1.1)}{B}=0.44322\,{\rm mm}.

**Answer.** Choose :math:`R>0.4432` mm to keep total
:math:`\alpha<3\,{\rm cm}^{-1}` under this model.

**Check.** The target radiation contribution is :math:`3-0.3=2.7`,
not 3. Linear interpolation of total loss is not the assumed physical model.

Problem 6.6 — Strip loading and the material-development sequence
-----------------------------------------------------------------

**Working.** In cross section, show a high-index guiding film on a
lower-index substrate and a patterned loading layer above it; the local
effective index rises beneath the strip. See the stripline diagram in
:doc:`ch03_theory_of_optical_waveguides`.

GaAs-on-GaAs can guide by carrier contrast but incurs free-carrier loss.
AlGaAs provides compositional index/gap control. Adding indium permits
longer-wavelength active regions, letting adjoining GaAs guides be more
transparent. A quaternary system adds freedom to tune bandgap and
lattice matching separately. MBE adds precise composition and thickness control.

**Answer.** The progression improves transparency, confinement,
emitter/guide compatibility, and interface quality.

**Check.** “Quaternary” alone does not guarantee lattice matching;
composition and the substrate still have to be chosen together.

Problem 6.7 — Cutback attenuation from a ten-percent length reduction
---------------------------------------------------------------------

**Working.** Equal launch conditions cancel the unknown coupling factor:

.. math::

   \frac{P(1.8)}{P(2.0)}=e^{\alpha(0.2)}=1.2,\qquad
   \alpha=\frac{\ln1.2}{0.2}=0.911608\,{\rm cm}^{-1}.

**Answer.** Approximately :math:`0.912\,{\rm cm}^{-1}`.

**Check.** The removed distance is 0.2 cm, not 10 cm or 10 percent
of the power. Shortening increases output, requiring positive attenuation.

Problem 6.8 — Separate coupling loss from propagation loss
----------------------------------------------------------

**Working.** In cutback measurements, retain the same launch while
measuring two or more lengths. Since
:math:`\ln P_{\rm out}=\ln(\eta_cP_{\rm in})-\alpha L`,
the slope gives propagation loss and the intercept gives coupling loss.

A second method samples calibrated side-scattered intensity along one
uniform guide. If scattering collection efficiency is constant,
its logarithmic slope also gives :math:`-\alpha`. Compare extrapolated
internal power with launched power to estimate coupling.

**Answer.** Use length-dependent transmission or calibrated spatial
decay, rather than assigning all insertion loss to propagation.

**Check.** Cutback fails if relaunching changes coupling; scattered-light
methods fail if local scattering or collection efficiency varies strongly.

Problem 6.9 — Halve a three-centimetre guide
--------------------------------------------

**Working.**

.. math::

   \alpha=\frac{\ln(5.5/5)}{3-1.5}
   =0.0635401\,{\rm cm}^{-1},\qquad
   s=4.3429448\alpha=0.275951\,{\rm dB/cm}.

**Answer.** (a) :math:`0.06354\,{\rm cm}^{-1}`.
(b) Approximately 0.2760 dB/cm.

**Check.** The 1.5 cm segment removed accounts for
:math:`10\log_{10}(1.1)=0.41393` dB.

Problem 6.10 — Free-carrier absorbed power
------------------------------------------

**Model.** Use the book's representative GaAs estimate at
1.15 micrometres, :math:`\alpha_{\rm fc}\simeq10^{-18}N`
with concentration in :math:`{\rm cm}^{-3}`. The exercise does not
specify wavelength or mobility, so this assumption is necessary.

**Working.** The lost fraction over 5 cm is :math:`1-e^{-5\alpha}`.

**Answer.** At :math:`N=10^{18}`, it is
:math:`1-e^{-5}=0.993262`, or 99.33 percent.
At :math:`N=10^{16}`, it is :math:`1-e^{-0.05}=0.0487706`,
or 4.877 percent.

**Check.** A hundredfold reduction in attenuation does not make
cumulative absorbed fractions differ by exactly a hundred when
the original sample is optically thick.

Problem 6.11 — Surface scattering and modal confinement
-------------------------------------------------------

**Working.** Roughness perturbs the dielectric boundary. To first order,
its scattering strength depends on the field sampled at that boundary
and on the roughness spatial spectrum. A tightly confined field with
small boundary amplitude couples less strongly to the rough interface.
A field with substantial exterior penetration is often more exposed.

**Answer.** In the intended comparison, the weakly confined mode
is more vulnerable to surface scattering.

**Check.** Tail length alone is not a universal loss predictor:
normalize both modes to equal power and compare their boundary fields
and the phase-matched roughness spectrum. Very near cutoff, changes
in normalization can invalidate a simple monotonic argument.
