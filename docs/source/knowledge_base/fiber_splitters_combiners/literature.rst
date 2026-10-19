Reviews and Original Research
==============================

This reading guide separates broad reviews from selected early papers and
original demonstrations. It does not assert that every listed paper was
the first invention of its technology. Authors, publication venues, years,
and identifiers were checked against publisher or author-institution
records. See :doc:`access` for exactly which full texts were obtained and
which summaries rely on abstracts or bibliographic records.

Download the :download:`BibTeX bibliography <references.bib>` for the
15 papers below. Patent records are listed separately in :doc:`patents`.


Recommended reviews
-------------------

Start with Fan for the overall combining problem, Stachowiak for physical
fiber components, and Birks for mode capacity and lanterns. Smit and van
Dam cover wavelength routing; Singh covers planar circuits; Lei and
colleagues focus on side-pump combiners.
Agarwal provides the historical overview of fiber-coupler constructions;
Marchetti and colleagues cover the separate fiber-to-chip interface problem.

.. _fiber-review-fan:

R1. Overall beam combining: Fan, 2005
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

T. Y. Fan, **Laser beam combining for high-power, high-radiance sources**,
*IEEE Journal of Selected Topics in Quantum Electronics* **11** (3),
567–577 (2005).
`DOI: 10.1109/JSTQE.2005.850241 <https://doi.org/10.1109/JSTQE.2005.850241>`_.

**Read for:** the power-versus-brightness distinction and the trade-offs
between spectral and coherent combining. This is the broadest starting
point here for the many-input problem; it is not a catalog of every
fiber splitter. The
`MIT Lincoln Laboratory record <https://www.ll.mit.edu/r-d/publications/laser-beam-combining-high-power-high-radiance-sources>`_
provides the author-hosted publication summary. A supplied full-text PDF
was checked for the combining requirements, coherent architectures, and
spectral/coherent comparison in sections I–III and V.

.. _fiber-review-stachowiak:

R2. Fiber power-combiner construction: Stachowiak, 2018
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dorota Stachowiak, **High-Power Passive Fiber Components for All-Fiber
Lasers and Amplifiers Application—Design and Fabrication**,
*Photonics* **5** (4), article 38 (2018).
`DOI: 10.3390/photonics5040038 <https://doi.org/10.3390/photonics5040038>`_.

**Read for:** tapered fused bundles, pump-only and pump/signal designs,
mode-field adaptors, fabrication constraints, and high-power performance.
The
`open-access publisher article <https://www.mdpi.com/2304-6732/5/4/38>`_
is the most directly relevant review here for building or specifying
physical all-fiber combiners.

.. _fiber-review-birks:

R3. Single-mode/multimode mapping: Birks et al., 2015
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

T. A. Birks, I. Gris-Sánchez, S. Yerolatsitis, S. G. Leon-Saval, and
R. R. Thomson, **The photonic lantern**, *Advances in Optics and
Photonics* **7** (2), 107–167 (2015).
`DOI: 10.1364/AOP.7.000107 <https://doi.org/10.1364/AOP.7.000107>`_.

**Read for:** adiabatic transitions between an array of SM cores and one
MM core, mode-number matching, losses, and applications. An
`author manuscript is available on arXiv <https://arxiv.org/abs/1503.02837>`_
with a `direct PDF <https://arxiv.org/pdf/1503.02837>`_.

.. _fiber-review-smit:

R4. WDM/AWG routing: Smit and van Dam, 1996
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

M. K. Smit and C. van Dam, **PHASAR-based WDM-devices: principles, design
and applications**, *IEEE Journal of Selected Topics in Quantum
Electronics* **2** (2), 236–250 (1996).
`DOI: 10.1109/2944.577370 <https://doi.org/10.1109/2944.577370>`_.

**Read for:** phased-array wavelength multiplexer/demultiplexer operation,
design, and routing applications. It explains how wavelength selectivity
changes the combining problem. The
`author-university repository record <https://research.tue.nl/en/publications/phasar-based-wdm-devices-principles-design-and-applications/>`_
links a published version; an alternative
`repository PDF endpoint <https://pure.tue.nl/ws/files/4339215/590297.pdf>`_
is included for access.

.. _fiber-review-singh:

R5. Planar-circuit background: Singh, 1999
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

B. R. Singh, **Silica Based Planar Lightwave Circuits: Status, Perspective
and Future**, *IETE Journal of Research* **45** (5–6), 345–353 (1999).
`DOI: 10.1080/03772063.1999.11416120 <https://doi.org/10.1080/03772063.1999.11416120>`_.

**Read for:** branching, switching, filtering, fabrication, and integration
in silica PLCs. The supplied full text describes cascaded Y-branches or
directional couplers for 1-by-N splitters, along with wavelength-routing
circuits. Treat its performance examples as historical. The journal year
is 1999, despite the publisher's later online-posting date.

.. _fiber-review-lei:

R6. Side-pump combiners: Lei et al., 2020
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chengmin Lei, Zhixian Li, Hui Zhang, Zilun Chen, and Jing Hou,
**Taper-fused side pump combiner for all-fiber lasers and amplifiers:
A review**, *Optics & Laser Technology* **130**, article 106353 (2020).
`DOI: 10.1016/j.optlastec.2020.106353 <https://doi.org/10.1016/j.optlastec.2020.106353>`_.

**Read for:** side-pump fabrication, performance, design parameters, and
power-scaling challenges. The supplied full text was consulted for input
NA sensitivity, taper geometry, backward coupling, and signal-beam
degradation. Section 4 explains why a continuous signal core still needs
careful control of heating and mechanical deformation during fabrication.

.. _fiber-review-agarwal:

R7. Historical fiber-coupler overview: Agarwal, 1987
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arun K. Agarwal, **Review of optical fiber couplers**, *Fiber and
Integrated Optics* **6** (1), 27–53 (1987).
`DOI: 10.1080/01468038708219344 <https://doi.org/10.1080/01468038708219344>`_.

**Read for:** a broad historical catalog of fused tapers, transmission
and reflection stars, micro-optic and grating splitters, offset and mixer
constructions, polished couplers, and early SM devices. The supplied PDF
contains the complete 27-page article plus a publisher cover. Figures 1–2
give its construction taxonomy; Figures 3–16 illustrate the historical
implementations. The characterization discussion on pages 45–47 explains
why launch-dependent MM devices need more than a single integrated power
measurement to predict cascaded behavior. Pages 47–49 distinguish SM
evanescent coupling from the MM taper description.

This is particularly useful for the **one-fiber-to-many** side of the
survey. Treat manufacturing and performance comparisons as historical,
not current specifications. Check the author's loss definition before
comparing a quoted value with per-branch insertion loss. The journal year
is **1987**; 2006 is the publisher's online-posting date, and 2013 is the
download date printed on the supplied cover.

.. _fiber-review-marchetti:

R8. Fiber-to-chip interfaces: Marchetti et al., 2019
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Riccardo Marchetti, Cosimo Lacava, Lee Carroll, Kamil Gradkowski, and
Paolo Minzioni, **Coupling strategies for silicon photonics integrated
chips [Invited]**, *Photonics Research* **7** (2), 201–239 (2019).
`DOI: 10.1364/PRJ.7.000201 <https://doi.org/10.1364/PRJ.7.000201>`_.

**Read for:** interfacing fibers to a silicon photonic splitter, AWG, or
other integrated circuit. The supplied 39-page review covers fiber types
and mode-field matching (section 2), edge coupling and inverse tapers
(section 3), grating coupling (sections 4–5), and packaging, alignment,
microlenses, and photonic wire bonds (section 6). Table 1 compares coupling
efficiency, polarization dependence, bandwidth, alignment tolerance, and
mode-field diameter. Its notes distinguish **experiments from simulations**
and the different loss thresholds used for bandwidth and tolerance.

A fiber-to-chip coupler transfers a field between a fiber and a waveguide;
it is not by itself a power splitter or a many-source combiner. For an
integrated device, budget the input and output interfaces separately from
on-chip splitting or routing. Section 6 also explains why fiber-array
alignment and adhesive curing can limit assembled performance even when
the bare coupling structure is efficient. The review is about silicon
photonics, not a qualification of silica PLCs or high-power fiber packages.


Selected original papers
-------------------------

.. _fiber-original-kawasaki1977:

O1. Multimode fused-fiber access coupler, 1977
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

B. S. Kawasaki and K. O. Hill, **Low-loss access coupler for multimode
optical fiber distribution networks**, *Applied Optics* **16** (7),
1794–1795 (1977).
`DOI: 10.1364/AO.16.001794 <https://doi.org/10.1364/AO.16.001794>`_.

**Why it matters:** an early original MM coupler experiment. The supplied
two-page paper describes twisted fibers fused and pulled into twin
biconical tapers, with 0.1–0.2 dB excess loss for the better devices. It
also discusses conversion to cladding-guided light, recapture by expanding
cores, and mode mixing. The related technical disclosure is
:ref:`fiber-patent-kawasaki`.

.. _fiber-original-kawasaki1981:

O2. Single-mode fused biconical taper, 1981
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

B. S. Kawasaki, K. O. Hill, and R. G. Lamont, **Biconical-taper single-mode
fiber coupler**, *Optics Letters* **6** (7), 327–328 (1981).
`DOI: 10.1364/OL.6.000327 <https://doi.org/10.1364/OL.6.000327>`_.

**Why it matters:** an early original SM coupler report. The supplied full
text describes a 30-device evaluation: a typical good device had 0.5 dB
excess loss; the best had 0.2 dB with equal splitting. Its test fiber
supported higher-order modes at the measurement wavelengths, so the
authors deliberately launched predominantly the fundamental mode. The
paper also measures wavelength-dependent branching ratios.

.. _fiber-original-hibino:

O3. Fiber-connected PLC splitter modules, 1994
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Y. Hibino, F. Hanawa, N. Takato, H. Nakagome, Y. Inoue, T. Miya, and
M. Yamaguchi, **Silica-based PLC splitters which satisfy reliability
requirements for more than 5000 hours**, *Conference on Optical Fiber
Communication*, 1994 OSA Technical Digest Series, volume 4, paper PD7
(1994).
`DOI: 10.1364/OFC.1994.PD7 <https://doi.org/10.1364/OFC.1994.PD7>`_.

**Why it matters:** an original report addressing 1-by-8 and 1-by-32
fiber-connected splitter modules and packaging reliability. These details
are supported by the publisher abstract; the complete reliability data
were not obtained.

.. _fiber-original-smit:

O4. Planar phased-array wavelength component, 1988
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

M. K. Smit, **New focusing and dispersive planar component based on an
optical phased array**, *Electronics Letters* **24** (7), 385–386 (1988).
`DOI: 10.1049/el:19880260 <https://doi.org/10.1049/el:19880260>`_.

**Why it matters:** an early phased-array dispersive component relevant
to AWG wavelength routing. See the
`author-university record <https://research.tue.nl/en/publications/new-focusing-and-dispersive-planar-component-based-on-an-optical-/>`_
and its
`repository PDF <https://pure.tue.nl/ws/files/4438613/590292.pdf>`_.

.. _fiber-original-kozlov:

O5. All-fiber laser beam combination, 1999
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V. A. Kozlov, J. Hernández-Cordero, and T. F. Morse, **All-fiber coherent
beam combining of fiber lasers**, *Optics Letters* **24** (24), 1814–1816
(1999).
`DOI: 10.1364/OL.24.001814 <https://doi.org/10.1364/OL.24.001814>`_.

**Why it matters:** the supplied full text describes a cleaved half of an
active-fiber fused coupler serving as the common output mirror of two
erbium-fiber laser cavities. Tuning a Bragg grating produced injection
locking; the reported spectra were limited by the analyzer's 0.05 nm
resolution. Cleave position and fusion geometry affected spatial
combination. This is a coupled-resonator experiment; adapting it to
separately packaged lasers or an output delivery pigtail requires further
design.

.. _fiber-original-leonsaval:

O6. Early photonic-lantern demonstration, 2005
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S. G. Leon-Saval, T. A. Birks, J. Bland-Hawthorn, and M. Englund,
**Multimode fiber devices with single-mode performance**, *Optics Letters*
**30** (19), 2545–2547 (2005).
`DOI: 10.1364/OL.30.002545 <https://doi.org/10.1364/OL.30.002545>`_.

**Why it matters:** the supplied full text demonstrates a grating filter
between two 19-port transitions. Its measured off-notch transmission was
only 3.4%: the authors intentionally did not match the 19 SM ports to the
roughly 710 supported MM spatial modes. The result establishes the
filtering concept and supports the mode-count argument; efficient matched
devices are developed in the later R3 review.

.. _fiber-original-morizur:

O7. Programmable spatial transformation, 2010
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jean-François Morizur, Lachlan Nicholls, Pu Jian, Seiji Armstrong,
Nicolas Treps, Boris Hage, Magnus Hsu, Warwick Bowen, Jiri Janousek,
and Hans-A. Bachor, **Programmable unitary spatial mode manipulation**,
*Journal of the Optical Society of America A* **27** (11), 2524–2531 (2010).
`DOI: 10.1364/JOSAA.27.002524 <https://doi.org/10.1364/JOSAA.27.002524>`_.

**Why it matters:** theory and an experimental programmable converter
using successive phase manipulations and propagation, relevant to MPLC
mode multiplexing. The
`downloaded author preprint <https://arxiv.org/abs/1005.3366>`_
uses the slightly different title *Programmable unitary spatial modes
manipulation*. Its experimental section distinguishes single-input
mode-conversion measurements from simulations of general multimode
transformations.
