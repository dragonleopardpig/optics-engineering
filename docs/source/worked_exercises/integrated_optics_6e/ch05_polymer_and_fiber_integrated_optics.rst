Chapter 5: Polymer and Fiber Integrated Optics
==============================================

Source: Hunsperger, sixth edition (2009), Problems 5.1--5.9,
printed page 103. Processing results refer to the measurements in the book.

Problem 5.1 — What controls a spun polymer-film thickness?
----------------------------------------------------------

**Working.** Centrifugal flow competes with viscous resistance while solvent
evaporates. Increasing polymer concentration or molecular weight normally
raises viscosity and leaves a thicker film. Increasing spin speed increases
outward flow and usually reduces thickness. Spin time matters until flow
and evaporation largely cease. Solvent volatility, temperature, and wetting
also affect the result; annealing removes residual solvent and relaxes strain.

**Answer.** Specify molecular weight, solution concentration and solvent,
spin speed/time, and anneal temperature/time. These form a process recipe,
not one universal thickness law.

**Check.** The concentration unit in Table 5.2 is solvent volume per gram
of polymer: increasing that number means a more dilute solution and
normally a thinner film.

Problem 5.2 — Arrayed-waveguide path difference and a consistency check
-----------------------------------------------------------------------

**Working.** Direct substitution in the book's printed Eq. (5.1), using
micrometres throughout, gives

.. math::

   \Delta L_{\rm printed}=
   \frac{(1.67)(7)(125)(1.55)}
        {(20)(8000)(0.001)}=14.1559\,\mu{\rm m}.

However Eq. (5.3) predicts the number of nonoverlapping output positions:

.. math::

   N_{\rm geom}=\frac{\lambda_0 f}{n_s dD}
   =\frac{(1.55)(8000)}{(1.67)(7)(125)}=8.486.

Thus the supplied geometry does not accommodate 20 channels in one free
spectral range. A standard dispersive phase calculation independently gives

.. math::

   n_{g,a}\Delta L=
   \frac{n_s dD\lambda_0}{f\,\delta\lambda}
   =283.117\,\mu{\rm m},

where :math:`n_{g,a}` is the array-waveguide group index, not the
number of channels.

**Answer.** The printed equation evaluates to 14.16 micrometres, but
the complete stated design is inconsistent. For example, assuming
:math:`n_{g,a}=1.67` gives a physical path difference of 169.53
micrometres and a free spectral range about 8.49 nm, insufficient for
twenty channels spaced 1 nm apart.

**Check.** The group index and phase-order condition must also be
specified for a realizable AWG. The two meanings of :math:`N` cannot
be interchanged to repair the printed expression silently.

Problem 5.3 — Increase AWG channel count
----------------------------------------

**Working.** The spatial range condition is
:math:`N_{\rm ch}\le\lambda_0f/(n_s dD)`. With fixed centre
wavelength and channel spacing, doubling capacity from an already
consistent baseline requires doubling :math:`f/(n_s dD)`.
Possible geometric changes are doubling focal radius, halving the
array pitch, halving output pitch, or combining smaller changes.
An index change can contribute but is constrained by the material platform.

**Answer.** Enlarge spatial free spectral range and ensure the spectral
free spectral range :math:`\lambda_0^2/(n_{g,a}\Delta L)` covers
the enlarged channel band. Adjust path increment/order and increase the
illuminated array aperture as needed to retain resolution and low crosstalk.

**Check.** Merely adding more output guides does not remove order
overlap. The original 5.2 geometry first needs correction even to reach
20 channels; its geometric capacity is only about 8.49.

Problem 5.4 — Polymer advantages over III–V materials
-----------------------------------------------------

**Working.** Solution deposition and low-temperature patterning can avoid
the demanding epitaxial growth required for crystalline III–V stacks.
Polymers can cover large areas, coat different substrates, and form
flexible or mechanically compliant interconnects. Composition and dopants
can tailor index, fluorescence, or electro-optic response. Lower index
contrast can also help match a fiber's mode size.

**Answer.** Processing simplicity, material/geometry flexibility, and
potentially inexpensive large-area fabrication are key advantages.

**Check.** These are not universal performance victories. Optical
absorption, thermal stability, aging, and attainable active-device
performance can favor semiconductors.

Problem 5.5 — Different polymer emission colours
------------------------------------------------

**Working.** Emission energy depends on the electronic structure of the
emitting molecule or conjugated segment, not solely on the bulk host.
Different fluorescent dopants or locally modified conjugation lengths
can therefore create regions with different transition energies.
Electrons and holes recombine in those emissive regions.

**Answer.** Pattern different emissive species or compositions in one
polymer platform. Each emits near :math:`\lambda=hc/\Delta E`.

**Check.** Distinct colours do not establish lasing. Energy transfer
between dopants and reabsorption can alter the observed spectrum, so
the emitters need suitable isolation and excitation.

Problem 5.6 — Recognize polymer lasing
--------------------------------------

**Working.** Measure output and spectrum while increasing pump strength.
Look for a threshold-like change in output slope, strong spectral
narrowing into cavity-selected lines, and directional coherent emission.
Test whether those features track an available optical feedback path.

**Answer.** The combination of gain overcoming cavity loss and
feedback-selected coherent oscillation establishes lasing.

**Check.** Amplified spontaneous emission can also narrow a spectrum
and produce superlinear output. Line narrowing alone is insufficient;
resolve cavity modes or measure coherence and feedback dependence.

Problem 5.7 — Fiber Bragg gratings and three fabrication routes
---------------------------------------------------------------

**Working.** An FBG is a longitudinal periodic effective-index
modulation. Forward and backward guided waves couple when
:math:`2\beta=2\pi m/\Lambda`, giving
:math:`\lambda_B=2N\Lambda/m`.

Three fabrication routes are two-beam interferometric UV exposure of
photosensitive fiber, phase-mask UV exposure, and focused point-by-point
laser inscription. The first two expose a periodic interference pattern;
the last writes individual perturbations directly.

**Answer.** Each method creates the required longitudinal index
periodicity rather than merely an absorbing stripe pattern.

**Check.** :math:`\lambda_B` uses the guided effective index and the
index-modulation period, not automatically the writing laser wavelength.

Problem 5.8 — Read a process-specific film thickness
----------------------------------------------------

**Working.** Match every supplied recipe parameter to Table 5.2:
280,000 molecular weight, 10 ml solvent per gram, 3000 rpm, 40 s,
and 110 degrees Celsius for 45 min. These identify sample 2.
Its measured average thickness is 10,710 angstroms.

.. math::

   t=10710\times10^{-4}\,\mu{\rm m}=1.071\,\mu{\rm m}.

**Answer.** Approximately 1.071 micrometres.

**Check.** This is an empirical recipe lookup, not an independent
prediction from spin speed alone. Samples with different concentration
cannot be substituted simply because their spin speeds match.

Problem 5.9 — Stern–Volmer constant from fluorescence data
----------------------------------------------------------

**Working.** Use the straightened plot in Fig. 5.14(b):

.. math::

   I_0/I=1+K_{\rm SV}[Q],\qquad
   K_{\rm SV}=\frac{\Delta(I_0/I)}{\Delta[Q]}.

The plotted line rises from roughly 1 at zero chloride to about 5.5
at 100 mM. Its slope is approximately
:math:`(5.5-1)/100=0.045\,{\rm mM}^{-1}`.

**Answer.** :math:`K_{\rm SV}\simeq0.045\,{\rm mM}^{-1}
=45\,{\rm M}^{-1}`, a graph-reading estimate.

**Check.** At 50 mM this predicts :math:`I/I_0\simeq1/3.25`,
consistent with the strongly quenched fluorescence. Using raw
fluorescence versus concentration as the linear plot would be incorrect.
