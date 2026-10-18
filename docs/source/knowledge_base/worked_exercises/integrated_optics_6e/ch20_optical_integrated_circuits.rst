Chapter 20: Optical Integrated Circuits
=======================================

Source: Hunsperger, sixth edition (2009), Problems 20.1--20.8,
printed page 447. Historical and technology-development questions
are interpreted relative to that edition.

Problem 20.1 — How aggregate rates reached terabits per second
--------------------------------------------------------------

**Working.** Aggregate throughput is approximately
:math:`R_{\rm total}=\sum_j R_j`.
DWDM raises the number of parallel wavelength channels; narrow,
stable lasers and selective filters reduce crosstalk between them.
Optical amplifiers restore many channels without per-channel
optical-electrical-optical conversion. Low-loss fiber and dispersion
control preserve signals over longer spans, while faster modulators
and receivers raise per-channel rate.

**Answer.** Channel parallelism, optical amplification, improved
fiber transmission, and high-speed sources/modulators/detectors act together.

**Check.** A terabit aggregate link does not imply every laser
was directly modulated at a terabit per second.

Problem 20.2 — Optical add/drop multiplexing
--------------------------------------------

**Working.** An OADM separates selected wavelength channels from
a multiplexed stream and directs them to a local drop port.
It inserts local signals at designated wavelengths through an add
port while forwarding the other channels.

**Answer.** It provides wavelength-selective access and routing
without demultiplexing, detecting, and regenerating every through channel.

**Check.** An OADM must control insertion loss, isolation, and
channel alignment. It is more selective than a power splitter that
sends every wavelength to every output.

Problem 20.3 — Dispersion-shifted fiber
---------------------------------------

**Working.** Total chromatic dispersion contains material and
waveguide contributions. Changing the refractive-index profile
and core geometry changes the latter, moving the wavelength
where their sum is zero.

**Answer.** Dispersion-shifted fiber places its low/zero-dispersion
region nearer a chosen communication band, historically toward
the low-loss 1.55 micrometre window.

**Check.** Low dispersion is not identical to low attenuation.
In DWDM systems exactly zero dispersion can also enhance
nonlinear mixing, motivating other dispersion profiles.

Problem 20.4 — Three integrated optical sensors
-----------------------------------------------

**Working.** A Mach–Zehnder interferometer senses changes in
optical path, so pressure or strain can be converted into phase.
An evanescent sensing guide changes response when analyte
index or absorption changes. A resonator or grating shifts
resonance with temperature or strain.

**Answer.** Examples are interferometric pressure/strain sensing,
evanescent chemical sensing, and resonant temperature sensing.

**Check.** Each example includes a transduction mechanism;
simply labelling an optical guide a “sensor” does not specify
what measurable quantity changes.

Problem 20.5 — First fiber communication links
----------------------------------------------

**Working.** The key distinction is between early optical
experiments and practical deployed low-loss fiber communication.
The development of low-loss fiber and semiconductor light
sources enabled the first commercial links during the 1970s.

**Answer.** The 1970s.

**Check.** Later high-capacity systems and modern dense
wavelength multiplexing are subsequent developments, not the
date of the first links.

Problem 20.6 — Blu-ray light source
-----------------------------------

**Working.** A shorter wavelength permits a smaller diffraction-limited
focused spot at a given numerical aperture, increasing the
disc's achievable recording density.

**Answer.** A blue-violet semiconductor laser diode near 405 nm,
using the GaN/InGaN material family.

**Check.** The short wavelength alone is not the complete
storage-density design; objective NA and recording-layer
properties also determine the spot and usable features.

Problem 20.7 — Dense wavelength-division multiplexing
-----------------------------------------------------

**Working.** Give independent signals closely spaced optical
carrier frequencies, combine them in one fiber, then separate
them with wavelength-selective devices at the receiver.
For :math:`M` equal-rate channels,
:math:`R_{\rm aggregate}\simeq M R_{\rm channel}`.

**Answer.** DWDM is wavelength multiplexing with closely spaced
channels requiring precise spectral control.

**Check.** Frequency and wavelength spacings are not numerically
interchangeable:
:math:`|\Delta\nu|\simeq c|\Delta\lambda|/\lambda_0^2`.
An amplifier's usable band limits the total channel allocation.

Problem 20.8 — Benefits of optical sensing
------------------------------------------

**Working.** A dielectric sensing head can provide electrical
isolation and little electromagnetic pickup. Light can interrogate
a small remote sensor through a fiber, and wavelength/time
multiplexing can combine several sensing positions.
Optical phase and resonance can be highly sensitive to small
geometrical or refractive changes.

**Answer.** Isolation, remote access, compactness, multiplexing,
and sensitive phase/spectral readout are possible advantages.

**Check.** Source drift, temperature cross-sensitivity, coupling
changes, and calibration still affect measurements. An optical
sensor is not automatically more accurate for every measurand.
