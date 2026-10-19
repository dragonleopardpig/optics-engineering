Selection, Specifications, and Verification
===========================================

The following choices are engineering recommendations from the mechanisms
in :doc:`splitting` and :doc:`combining`. Vendor links illustrate component
classes; they do not establish a final qualified design.


Choose an architecture
-----------------------

.. list-table:: Match the optical requirement before selecting a supplier
   :header-rows: 1
   :widths: 33 29 38

   * - Requirement
     - Starting architecture
     - Confirm before proceeding
   * - One laser to two fibers, including a small monitor tap
     - SM or PM FBT coupler
     - Split ratio over the laser band, PER, and branch power budget
   * - Same spectrum in many outputs
     - PLC splitter or fused-coupler tree
     - Port uniformity, worst-path insertion loss, fiber and power rating
   * - Broadband light to several MM fibers
     - MM fused splitter or packaged free-space distribution
     - Actual launch distribution and branch near-/far-field behavior
   * - Several distinct laser wavelengths into one core
     - WDM or dichroic combiner with fiber coupling
     - Passbands, isolation, and output-fiber guidance at every wavelength
   * - Two polarized lasers at the same wavelength; both output axes acceptable
     - PBC with aligned PM inputs
     - Output polarization requirements and downstream polarization loss
   * - Many independent sources; an MM output is acceptable
     - Tapered bundle or MM signal combiner
     - Acceptance capacity, output beam quality, and thermal design
   * - Multiple pumps and one seed for a fiber amplifier
     - Pump/signal combiner
     - Pump-to-cladding and signal-to-core paths, splice geometry, direction
   * - Several SM channels in the spatial modes of one fiber
     - Photonic lantern or mode multiplexer
     - Mode count, mapping, modal loss, and channel crosstalk
   * - Same wavelength, one spatial mode, one polarization, high combined power
     - Coherent combiner
     - Mutual coherence, phase control, temporal overlap, and final-fiber limits
   * - Several sources sharing an output at different times
     - Optical switch
     - Switching speed, extinction, and selected-path power rating


A specification to send suppliers
---------------------------------

Record the following before requesting a component or custom design:

1. **Optical spectrum:** each center wavelength, linewidth, spectral shape,
   tuning range, and drift. Identify whether different inputs are mutually
   coherent and whether relative phase control is available.
2. **Power and timing:** power per input and total output; CW or pulsed;
   pulse energy, duration, repetition rate, and peak power. For coherent
   pulses, specify delay and dispersion tolerances.
3. **Fiber interfaces:** exact fiber types and required output; core and
   cladding diameters, NA, mode-field diameter, and supported modes at each
   wavelength. Distinguish common core, inner cladding, and multiple cores.
4. **Polarization:** arbitrary or linear input, required PER, PM axes and
   connector keys, and permitted output polarization state.
5. **Transfer targets:** split ratios, per-path insertion loss, excess loss,
   uniformity, isolation, return loss, and acceptable channel crosstalk.
   Define wavelength, polarization, launch, temperature, and reference planes.
6. **Output quality:** total power alone, specified NA, near-field profile,
   beam parameter product, :math:`M^2`, or a specified guided mode.
7. **Packaging:** fusion splices or exact connector types, pigtail lengths,
   bend radius, cooling, operating environment, and backward-light exposure.

Power ratings must apply to the assembled configuration. A bare or
fusion-spliced device can have a different limit from a connectorized
version. Return loss is not an optical-isolator rating. A component with
low reflection can still transmit backward light from another source.

For a chip-based device, separate the fiber-to-chip interfaces from the
on-chip splitter or wavelength router. In a fiber-input/fiber-output
measurement, the input coupling, on-chip transmission, and output coupling
all contribute to the measured branch loss; do not add interface losses
again if they are already included in the packaged-device specification.
:ref:`fiber-review-marchetti` covers mode matching, fiber-array alignment,
and curing-induced movement in silicon photonic packages. Its Table 1
distinguishes measured from simulated results and flags different loss
thresholds for bandwidth and alignment tolerance.


Read the quoted metrics carefully
---------------------------------

.. list-table:: Common specification traps
   :header-rows: 1
   :widths: 28 72

   * - Quoted metric
     - Interpretation needed
   * - "Low-loss splitter"
     - Excess loss can be low while the intended division still costs each branch 10 log10(N) dB.
   * - "Combining efficiency"
     - Specify useful power in the required output mode divided by total launched input power; separate core and cladding power.
   * - "Single-mode output"
     - State wavelength range and polarization count; one spatial mode may carry two polarizations and many wavelengths.
   * - "High power"
     - Distinguish per-port, total, CW, pulse energy, peak power, and backward-power limits.
   * - "Bidirectional"
     - Confirm the tested ports, modes, and operating conditions in each direction.
   * - "Uniform outputs"
     - Integrated powers, spectra, polarization, spatial profiles, and timing are different requirements.


Acceptance measurements
------------------------

Start with each source separately. Measure the desired output, all
accessible unused ports, and reflected or backward power under the stated
conditions. For a router or splitter, form a power-transfer table
:math:`T_{kj}=P_{k,\rm out}/P_{j,\rm in}`. Repeat for relevant wavelengths,
polarizations, launch conditions, bends, and temperatures.

For incoherent sources, simultaneous operation should agree with the
sum of the individual transmitted powers within the uncertainty and
stability limits. Coherent sources require field or interference
measurements instead: sweep phase, observe bright and dark outputs, and
measure stability during operation. A power-transfer table alone does
not capture phase.

For a mode-selective MM coupler, a transfer table measured with one launch
distribution may not predict a cascade in which later stages see a
different modal population. The characterization discussion in
:ref:`fiber-review-agarwal` motivates recording the launch conditions and,
where necessary, measuring mode-resolved transfer as well as total power.

For MM and pump devices, measure output near and far fields or an
appropriate modal/beam-quality metric, and distinguish core power from
cladding power. Check temperatures and rejected-light paths at the
intended load. Missing guided power can escape as radiation as well as
become heat, so do not equate the entire optical deficit with package
absorption without measurement.

For a claimed efficient reverse combiner, ask for the port diagram, the
input coherence and polarization conditions, and the exact output modes
included in the efficiency measurement. These details resolve most
apparent contradictions between reciprocity and power conservation.
