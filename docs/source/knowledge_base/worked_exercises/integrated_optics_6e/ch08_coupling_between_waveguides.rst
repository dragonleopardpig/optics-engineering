Chapter 8: Coupling Between Waveguides
======================================

Source: Hunsperger, sixth edition (2009), Problems 8.1--8.8,
printed pages 167--168.

Coupled-mode model
------------------

For one excited input, uniform power loss :math:`\alpha` in each
guide, coupling coefficient :math:`\kappa`, and mismatch
:math:`\Delta\beta`, write

.. math::
   :label: integrated-coupler

   \frac{P_1}{P_{\rm in}}=
   e^{-\alpha L}\frac{\kappa^2}{g^2}\sin^2(gL),\qquad
   g=\sqrt{\kappa^2+(\Delta\beta/2)^2}.

The other output is :math:`e^{-\alpha L}-P_1/P_{\rm in}`.

.. figure:: /_static/knowledge_base/worked_exercises/integrated_optics_6e/directional_coupler.svg
   :alt: Sinusoidal exchange between phase-matched guides and reduced transfer with detuning.
   :width: 100%

   Phase matching permits complete exchange; mismatch limits it.

Problem 8.1 — Detuning for a zero-transfer output
-------------------------------------------------

**Working.** For the shortest complete-transfer coupler,
:math:`\kappa L=\pi/2`. The first nonzero detuned zero occurs at
:math:`gL=\pi`. Thus

.. math::

   (\Delta\beta/2)^2=(\pi/L)^2-(\pi/2L)^2,
   \qquad |\Delta\beta|=\sqrt3\,\pi/L.

**Answer.** The shortest-device result is :math:`\sqrt3\pi/L`.
More generally, if the unperturbed device has
:math:`\kappa L=(m+\frac12)\pi`, its first higher zero
:math:`gL=(m+1)\pi` requires
:math:`|\Delta\beta|=(\pi/L)\sqrt{4m+3}`.

**Check.** The two conditions in the question must use compatible
orders; setting the same symbols equal without squaring loses the
order dependence.

Problem 8.2 — Required effective-index change
---------------------------------------------

**Working.** Holding one guide fixed gives
:math:`\Delta\beta=k_0\Delta N`. Divide the shortest-device
answer of 8.1 by :math:`k_0`:

.. math::

   |\Delta N|=\frac{\sqrt3\pi}{k_0L}
   =\frac{\sqrt3\lambda_0}{2L}.

**Answer.** This is the required **effective-index** difference.

**Check.** A bulk material-index change equals this only for
unit optical overlap. Otherwise include the perturbation overlap
between the applied field and the guided mode.

Problem 8.3 — Numerical detuning for a centimetre coupler
---------------------------------------------------------

**Working.** Use :math:`\lambda_0=0.9\,\mu{\rm m}` and
:math:`L=10^4\,\mu{\rm m}`:

.. math::

   |\Delta N|=\frac{\sqrt3(0.9)}{2(10^4)}
   =7.79423\times10^{-5}.

**Answer.** Approximately :math:`7.79\times10^{-5}`.

**Check.** Index is dimensionless; using 1 for the length while
leaving wavelength in micrometres would give an erroneous factor of 10,000.

Problem 8.4 — Which index gives stronger coupling?
--------------------------------------------------

**Working.** With otherwise identical guides and cladding, a larger
core index normally strengthens confinement and shortens the
evanescent tail. The coupling integral samples the other guide's
field in that tail.

**Answer.** Under this fixed-cladding, comparable-mode assumption,
the lower-index pair B has greater tail overlap and generally larger
:math:`\kappa`.

**Check.** Core index alone does not establish a universal theorem:
cladding index, mode order, normalization, and geometry must be held
consistent. Near a mode cutoff, compare the actual overlap integrals.

Problem 8.5 — Lossy three-decibel divider
-----------------------------------------

**Working.** At phase match, equal surviving outputs require
:math:`\kappa L=\pi/4`. With :math:`\kappa=4\,{\rm cm}^{-1}`,

.. math::

   L=\pi/16=0.196350\,{\rm cm},\qquad
   P_0/P_{\rm in}=P_1/P_{\rm in}
   =\tfrac12e^{-0.6L}\simeq0.44443.

Doubling length makes :math:`\kappa(2L)=\pi/2`.

**Answer.** The shortest divider is 1.9635 mm long.
At double length the ideal through output is zero and the cross output
is :math:`e^{-0.6(2L)}\simeq0.79008` of input power.

**Check.** “3 dB divider” means equal splitting of surviving power;
with propagation loss neither output receives exactly half the input.

Problem 8.6 — Nanometre-unit coupling length
--------------------------------------------

**Working.** The supplied coupling coefficient already contains
the geometric and material information. Therefore

.. math::

   L_{3{\rm dB}}=\frac{\pi}{4\kappa}
   =\frac{\pi}{4(1.229\times10^{-5})}\,{\rm nm}
   \simeq6.3906\times10^4\,{\rm nm}.

**Answer.** Approximately 63.91 micrometres.

**Check.** The full-transfer length is twice this value. The other
waveguide dimensions need not be inserted a second time.

Problem 8.7 — Why synchronous coupling can transfer all power
-------------------------------------------------------------

**Working.** Two identical isolated-guide modes combine into even and
odd supermodes with propagation constants approximately
:math:`\beta\pm\kappa`. Exciting one guide creates an equal
superposition. Their relative phase grows as :math:`2\kappa z`.
At :math:`2\kappa L=\pi`, destructive interference cancels one
guide's field and constructive interference reinforces the other.

**Answer.** With phase match, nonzero overlap, and negligible loss,
complete transfer occurs at :math:`L=\pi/(2\kappa)`.

**Check.** Detuning reduces the maximum transferable fraction to
:math:`\kappa^2/[\kappa^2+(\Delta\beta/2)^2]`.
The effect is coherent mode beating, not photon absorption and re-emission.

Problem 8.8 — Control the coupling coefficient
----------------------------------------------

**Working.** During fabrication, adjust gap, ridge width/height,
etch depth, and material contrast. A smaller gap or more extended
tails generally increase the overlap integral. After fabrication,
electro-optic, thermo-optic, carrier, or mechanical perturbations can
change mode confinement and therefore coupling.

**Answer.** Control the spatial overlap to change :math:`\kappa`.
Use differential index tuning to introduce :math:`\Delta\beta`
when the goal is switching rather than changing overlap itself.

**Check.** Changing transfer by detuning is not automatically a change
in :math:`\kappa`. The two quantities appear separately in
:eq:`integrated-coupler`.
