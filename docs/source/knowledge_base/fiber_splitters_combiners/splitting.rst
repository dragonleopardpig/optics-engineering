Splitting One Fiber into Several Fibers
=======================================

First decide whether every branch needs the same spectrum, or whether
different branches should receive different wavelengths, polarizations,
or spatial modes. Only the first case is ordinary power splitting.

.. contents:: On this page
   :local:
   :depth: 2


Fused-fiber power splitters
---------------------------

An FBT coupler is made by heating and stretching adjacent fibers into a
coupled taper. A 2-by-2 device exposes both ports at each end. A packaged
1-by-2 device may terminate one port internally. Coupling length and
geometry determine the split ratio; cascades or multi-fiber structures
provide more outputs.

.. figure:: /_static/knowledge_base/fiber_splitters_combiners/01_fused_coupler.svg
   :alt: Two tapered fibers share a coupling region; light entering one fiber reaches both through and coupled outputs, while the second input remains unused.
   :width: 100%
   :align: center

   An FBT coupler exchanges guided optical power in a shared waist.
   The blue paths indicate power transfer, rather than individual rays
   or a calculated field distribution.

This is a useful starting point for a two-way split, a monitoring tap, or
a small distribution tree. Choose single-mode (SM), polarization-maintaining
(PM), or multimode (MM) fiber to match the source. PM fiber preserves
properly launched polarization; it does not turn unpolarized light into
one linear polarization.

Early primary sources are
`Kawasaki and Hill (1977) <https://doi.org/10.1364/AO.16.001794>`_ for MM
access couplers and
`Kawasaki, Hill, and Lamont (1981) <https://doi.org/10.1364/OL.6.000327>`_
for SM fused biconical tapers. Both full papers were checked. Their
reported excess losses concern specific experimental devices and launch
conditions, rather than a universal specification for modern splitters;
see the detailed notes in :doc:`literature`.

For current component examples, Thorlabs documents
`1550 nm 2-by-2 fused couplers <https://www.thorlabs.us/newgrouppage9.cfm?objectgroup_ID=9152>`_
and
`1550 nm PM 1-by-2 couplers <https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=10015>`_.
These examples establish available device categories, not suitability for
an unspecified laser. Check the exact fiber, operating band, split-ratio
tolerance, and termination-dependent power rating.

.. figure:: /_static/knowledge_base/fiber_splitters_combiners/02_star_coupler.svg
   :alt: One illuminated fiber input feeds a fused mixing region and distributes light to three output fibers; other inputs are inactive.
   :width: 100%
   :align: center

   A conceptual transmission star distributes an input among several
   output ports. Reflection and hybrid stars use different port layouts;
   :doc:`patents` describes the looped-fiber implementation in P2.


PLC and other integrated splitters
----------------------------------

A PLC uses planar waveguides, often silica on silicon, with branching
structures to distribute light to fiber arrays. Cascaded Y-junctions are
one implementation; integrated directional couplers and multimode
interference (MMI) structures provide other splitting mechanisms. Here
"multimode interference" describes the internal waveguide region; the
external pigtails can still be single-mode.

.. figure:: /_static/knowledge_base/fiber_splitters_combiners/03_planar_splitters.svg
   :alt: Three planar implementations show a cascaded Y-branch tree feeding four fibers, two adjacent coupled waveguides, and a wider multimode-interference region forming two output images.
   :width: 100%
   :align: center

   Y-branches divide the path geometrically, directional couplers exchange
   power between neighboring guides, and MMI devices use internal modal
   interference. The same tree topology can also be built from discrete
   fused couplers. See :ref:`fiber-review-singh` for planar-circuit context.

PLC packaging is attractive when many outputs must fit into one module.
Do not assume that a telecom splitter is suitable for visible light,
ultrashort pulses, or high-power fiber lasers. Material transparency,
waveguide modes, fiber coupling, dispersion, and thermal behavior all
need to match the application.

An early experimental reference is
`Hibino et al. (1994) <https://doi.org/10.1364/OFC.1994.PD7>`_: its
publisher abstract describes fiber-connected 1-by-8 and 1-by-32 silica PLC
modules and reliability evaluation. For background, see
:ref:`fiber-review-singh`. An industrial example is
`Corning's PLC splitter family <https://www.corning.com/oem-solutions/worldwide/en/home/products-solutions/optical-communication-components/taps-couplers-splitters/plc-splitters.html>`_.


Packaged free-space splitting
-----------------------------

Another arrangement collimates the input fiber, divides the beam with
beamsplitters or a diffractive optical element, and focuses each branch
into an output fiber. It can accommodate unusual wavelengths or ratios,
but each fiber launch adds an alignment and mode-matching problem. Its
engineering trade-off is optical flexibility against alignment,
packaging, coating, and coupling losses. See
:doc:`../active_fiber_alignment` for the overlap calculation.

.. figure:: /_static/knowledge_base/fiber_splitters_combiners/04_free_space_splitters.svg
   :alt: A collimated fiber beam is partially reflected and transmitted into two separately focused fiber outputs; a second panel shows a diffractive element feeding several fiber launches.
   :width: 100%
   :align: center

   Free-space splitting requires a separate fiber launch for each output.
   A beamsplitter divides reflection and transmission; a diffractive
   optical element creates several orders that are relayed into a fiber
   array. Optical paths are schematic, not a ray-traced prescription.

For a coherent laser, splitting also establishes relative branch phases.
Separate branch lengths then introduce phase drift and pulse delays.
Equal powers alone do not guarantee equal arrival times or stable
interference downstream.


Splitting by wavelength, polarization, or mode
----------------------------------------------

* **WDM demultiplexer:** each output receives a selected spectral band.
  The reverse direction is wavelength combining. The AWG approach is
  reviewed in :ref:`fiber-review-smit`.
* **Polarization splitter:** two outputs receive orthogonal polarization
  components. Their power ratio depends on the input polarization.
  A
  `fused-fiber polarization splitter <https://www.thorlabs.com/fused-fiber-polarization-combinerssplitters-3-pm-ports>`_
  is a concrete implementation.
* **Photonic lantern or mode demultiplexer:** several SM ports receive
  a mapping of a multimode input field. This does not inherently give
  equal powers or identical fields in every port. See
  :ref:`fiber-review-birks` and :ref:`fiber-original-morizur`.

The :ref:`wavelength-routing <fiber-figure-wdm>`,
:ref:`polarization <fiber-figure-polarization>`, and
:ref:`photonic-lantern <fiber-figure-lantern>` diagrams on the combining
page also illustrate the corresponding splitting functions when the
specified ports and modes are used in reverse.


Power and loss accounting
-------------------------

For an ideal equal splitter with :math:`N` outputs, each branch receives
:math:`P_{\rm in}/N`. Define branch insertion loss and splitter excess
loss separately:

.. math::

   IL_j=-10\log_{10}\!\left(\frac{P_j}{P_{\rm in}}\right),
   \qquad
   EL=-10\log_{10}\!\left(\frac{\sum_jP_j}{P_{\rm in}}\right).

Here all powers are measured at explicitly defined reference planes.
For equal branches, :math:`IL_j=10\log_{10}N+EL`. Unequal devices require
their actual branch transmissions. Manufacturer specifications may include
or exclude connectors; retain the same convention throughout the budget.
Thorlabs' `coupler documentation <https://www.thorlabs.us/newgrouppage9.cfm?objectgroup_ID=9152>`_
also distinguishes insertion loss from excess loss.

.. list-table:: Ideal loss per equal branch, before excess loss
   :header-rows: 1
   :widths: 30 35 35

   * - Number of outputs
     - Power in each branch
     - Ideal branch loss
   * - 2
     - 50%
     - 3.01 dB
   * - 4
     - 25%
     - 6.02 dB
   * - 8
     - 12.5%
     - 9.03 dB
   * - 16
     - 6.25%
     - 12.04 dB
   * - 32
     - 3.125%
     - 15.05 dB
   * - 64
     - 1.5625%
     - 18.06 dB

**Calculated example.** A 100 mW input, eight equal outputs, and 0.6 dB
excess loss give

.. math::

   P_j=\frac{100\,\mathrm{mW}}{8}10^{-0.6/10}
       =10.89\,\mathrm{mW}.

The total output is 87.10 mW. The 9.03 dB ideal division is redistribution
of useful power, not 9.03 dB of absorption inside the package. For a
cascaded tree, add the branch insertion losses along each actual path;
do not add the ideal split penalty a second time.


Multimode launch sensitivity
----------------------------

An MM splitter's ratio can change when the input mode distribution changes.
Core size and nominal numerical aperture (NA) do not specify that
distribution. A tightly focused laser launch and a broadly filled
illumination fiber can produce different results through the same
component. Thorlabs explicitly discusses this for its
`step-index MM couplers <https://www.thorlabs.us/newgrouppage9.cfm?objectgroup_id=11213>`_.
Specify the launch geometry, fiber bends, spectral bandwidth, and whether
the requirement concerns total power, near-field uniformity, or speckle.
An equal integrated-power split need not produce identical output
intensity patterns.
