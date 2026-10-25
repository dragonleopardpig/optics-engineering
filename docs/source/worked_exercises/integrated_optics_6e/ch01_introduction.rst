Chapter 1: Introduction
=======================

Source: Hunsperger, sixth edition (2009), Chapter 1, Problems 1.1--1.4,
printed page 15. Each explanatory answer connects the claimed advantage
to the mechanism producing it.

Problem 1.1 — Four advantages of fiber interconnects
----------------------------------------------------

**Task.** Compare an optical fiber link with a metallic signal connection.

**Working.** Four distinct advantages are:

1. **Electrical isolation.** A dielectric fiber carries no conduction current
   between endpoints, removing the conducting path responsible for ground-loop
   currents and electrical shorts.
2. **Resistance to electromagnetic pickup.** Information travels as guided
   light rather than a current induced in a long metal conductor. External RF
   fields therefore do not couple into it as they do into an unshielded wire.
3. **Capacity and reach.** Low optical attenuation permits long spans, while
   independent wavelength channels carry several data streams in one fiber.
4. **Size and mass.** Thin fibers provide many channels without the mass of
   a comparable bundle of conductors and electromagnetic shields.

**Answer.** Isolation, EMI resistance, transmission capacity/reach, and
small size/mass are four separate benefits.

**Check.** Isolation concerns a conducting path; EMI resistance concerns
unwanted coupling. Transmitters and receivers still require electrical
power, and their electronics can remain sensitive to EMI.

Problem 1.2 — Advantages of optical integrated circuits
-------------------------------------------------------

**Task.** Identify four benefits of integrated optical signal processing.

**Working.** Optical waveguides support a broad carrier-frequency range,
making high aggregate bandwidth possible. Wavelength-selective filters
separate independent channels; for :math:`M` channels of rate :math:`B`,
the aggregate rate is approximately :math:`MB`.

A directional coupler transfers or divides optical power between adjacent
guides without separately aligning a chain of bulk optical components.
Lithographically defined paths also maintain relative alignment and allow
many devices to be fabricated together.

**Answer.** Bandwidth, wavelength multiplexing, compact coupling/switching,
and reproducible integrated alignment are four defensible advantages.

**Check.** The last two compare most directly with discrete optics.
The optical carrier does not remove bandwidth limits in an electrical
driver or receiver; power savings depend on the whole system.

Problem 1.3 — Hybrid and monolithic integration
-----------------------------------------------

**Task.** Explain the two integration strategies and their tradeoffs.

**Working.** Monolithic integration fabricates relevant functions within
a common material/device platform. Hybrid integration assembles separately
fabricated components or material platforms and connects them optically.

.. list-table:: Consequences of the integration choice
   :header-rows: 1

   * - Issue
     - Monolithic
     - Hybrid
   * - Material choice
     - Compatible device processes required
     - Optimize laser, guide, and detector separately
   * - Alignment
     - Defined largely by fabrication
     - Assembly interfaces need alignment control
   * - Development
     - Process compatibility and yield are difficult
     - Reuse mature component technologies
   * - Production
     - Batch processing can lower assembly cost
     - Packaging and coupling can dominate cost/loss

**Answer.** Hybrid integration trades extra interfaces for material freedom;
monolithic integration trades process constraints for reproducible alignment
and potentially simpler assembly.

**Check.** A single package does not establish monolithic integration.
The distinction is how devices are fabricated and combined.

Problem 1.4 — Why III–V compound semiconductors are useful
----------------------------------------------------------

**Working.** A suitable direct-gap composition permits efficient radiative
electron-hole recombination and optical gain without a momentum-changing
phonon. Alloy composition changes the gap and hence the emission wavelength:

.. math::

   \lambda_0\simeq hc/E_g.

A transparent passive guide needs a gap larger than the photon energy,
whereas an interband detector needs a gap no larger than that energy.
Alloying therefore supplies different functions in compatible
heterostructures. Index steps confine light; band offsets confine injected
carriers; lattice matching reduces interface defects.

**Answer.** Direct-gap emission, adjustable gap and index, useful
electro-optic properties, and compatible heteroepitaxy make GaAs-based
and InGaAsP-based systems valuable.

**Check.** Not every alloy composition remains direct-gap or lattice-matched.
The claim applies to suitable composition ranges.
