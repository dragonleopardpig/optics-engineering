Chapter 23: Optical Interconnects and Switches
===============================================

Source: Saleh and Teich, *Fundamentals of Photonics*, second edition,
Chapter 23.

Section 23.1 Formulation — Interconnection Matrix
-------------------------------------------------

In optical communication and photonic integrated circuits, multi-port optical
couplers and routers connect :math:`M` input channels to :math:`N` output channels.
In *Fundamentals of Photonics* (Saleh & Teich, 2nd ed., Section 23.1), the
interconnection matrix is introduced via three baseline equations:

1. **Coherent field superposition** (Eq. 23.1-1):

   .. math::

      U_\ell^{(o)} = \sum_{m=1}^M T_{\ell m} U_m^{(i)}

2. **Ideal 3-dB coupler example** (Eq. 23.1-2):

   .. math::

      \mathbf{T} = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & j \\ j & 1 \end{bmatrix}

3. **Incoherent power distribution** (Eq. 23.1-3):

   .. math::

      P_\ell^{(o)} = \sum_{m=1}^M |T_{\ell m}|^2 P_m^{(i)}

While these three relations provide the starting point, practical photonic
design requires:

* The explicit **coherent output power** including cross-channel interferometric
  beating terms.
* The physical constraints imposed by **energy conservation**, which dictate that
  lossless transmission matrices :math:`\mathbf{T}` are unitary and the corresponding
  power transfer matrices :math:`\mathbf{S}` are orthostochastic.
* A unified formulation using the **mutual coherence matrix** (or cross-spectral
  density matrix) that smoothly bridges fully coherent, partially coherent, and
  fully incoherent regimes.

1. Coherent Multiport Fields and Output Power
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1 Matrix Formulation of Linear Superposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let the monochromatic (or quasi-monochromatic) complex field amplitudes at the
:math:`M` input ports and :math:`N` output ports be represented by column vectors:

.. math::

   \mathbf{U}^{(i)} = \begin{bmatrix} U_1^{(i)} \\ U_2^{(i)} \\ \vdots \\ U_M^{(i)} \end{bmatrix} \in \mathbb{C}^M, \qquad
   \mathbf{U}^{(o)} = \begin{bmatrix} U_1^{(o)} \\ U_2^{(o)} \\ \vdots \\ U_N^{(o)} \end{bmatrix} \in \mathbb{C}^N.

For any linear, time-invariant optical interconnect, the output field vector is
related to the input field vector by an :math:`N \times M` complex interconnection
matrix :math:`\mathbf{T}`:

.. math::
   :label: eq-coherent-field-matrix

   \mathbf{U}^{(o)} = \mathbf{T} \mathbf{U}^{(i)}, \qquad
   U_\ell^{(o)} = \sum_{m=1}^M T_{\ell m} U_m^{(i)}.

Each matrix element :math:`T_{\ell m}` is a complex transmission coefficient
characterizing the path from input port :math:`m` to output port :math:`\ell`:

.. math::

   T_{\ell m} = |T_{\ell m}| e^{j \theta_{\ell m}},

where :math:`|T_{\ell m}|` represents the field amplitude coupling ratio and
:math:`\theta_{\ell m} = \arg(T_{\ell m})` is the optical phase delay through the
device between port :math:`m` and port :math:`\ell`.


1.2 Expansion of Coherent Output Power
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each input field phasor can be expressed in terms of its optical power
:math:`P_m^{(i)} = |U_m^{(i)}|^2` and initial phase :math:`\phi_m`:

.. math::

   U_m^{(i)} = \sqrt{P_m^{(i)}} \, e^{j \phi_m}.

The optical power emerging at output port :math:`\ell` is the squared modulus of the
total superposed field:

.. math::

   P_\ell^{(o)} = |U_\ell^{(o)}|^2 = \left( \sum_{m=1}^M T_{\ell m} U_m^{(i)} \right) \left( \sum_{k=1}^M T_{\ell k}^* U_k^{(i)*} \right).

Expanding the double summation into self-power terms (:math:`m = k`) and mutual
cross terms (:math:`m \neq k`):

.. math::

   P_\ell^{(o)} = \sum_{m=1}^M |T_{\ell m}|^2 |U_m^{(i)}|^2 + \sum_{m=1}^M \sum_{k \neq m}^M T_{\ell m} T_{\ell k}^* U_m^{(i)} U_k^{(i)*}.

Pairing complex conjugate indices (:math:`m < k`) gives the complete coherent
power relation:

.. math::
   :label: eq-coherent-power-complete

   \boxed{P_\ell^{(o)} = \underbrace{\sum_{m=1}^M |T_{\ell m}|^2 P_m^{(i)}}_{\text{Direct power contribution}} + \underbrace{2 \sum_{m < k}^M |T_{\ell m}| |T_{\ell k}| \sqrt{P_m^{(i)} P_k^{(i)}} \cos\Big( (\phi_m - \phi_k) + (\theta_{\ell m} - \theta_{\ell k}) \Big)}_{\text{Interferometric cross-terms}}.}

.. note::

   * The first summation matches the incoherent power equation (Eq. 23.1-3).
   * The second summation represents **constructive and destructive interference**.
     It depends directly on the relative input phases :math:`\Delta \phi_{mk} = \phi_m - \phi_k`
     as well as the internal device differential phase delays :math:`\Delta \theta_{\ell, mk} = \theta_{\ell m} - \theta_{\ell k}`.


1.3 Example: Symmetrical 2 × 2 3-dB Coupler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an ideal symmetric 3-dB directional coupler (Saleh & Teich Eq. 23.1-2):

.. math::

   \mathbf{T} = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & j \\ j & 1 \end{bmatrix}
   = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & e^{j\pi/2} \\ e^{j\pi/2} & 1 \end{bmatrix}.

The output fields are:

.. math::

   U_1^{(o)} = \frac{1}{\sqrt{2}}\left( U_1^{(i)} + j U_2^{(i)} \right), \qquad
   U_2^{(o)} = \frac{1}{\sqrt{2}}\left( j U_1^{(i)} + U_2^{(i)} \right).

Applying Eq. :eq:`eq-coherent-power-complete`:

.. math::

   P_1^{(o)} &= \frac{1}{2} P_1^{(i)} + \frac{1}{2} P_2^{(i)} + \sqrt{P_1^{(i)} P_2^{(i)}} \cos\left( (\phi_1 - \phi_2) - \frac{\pi}{2} \right) \\
             &= \frac{1}{2}\left( P_1^{(i)} + P_2^{(i)} \right) + \sqrt{P_1^{(i)} P_2^{(i)}} \sin(\phi_1 - \phi_2),

.. math::

   P_2^{(o)} &= \frac{1}{2} P_1^{(i)} + \frac{1}{2} P_2^{(i)} + \sqrt{P_1^{(i)} P_2^{(i)}} \cos\left( (\phi_1 - \phi_2) + \frac{\pi}{2} \right) \\
             &= \frac{1}{2}\left( P_1^{(i)} + P_2^{(i)} \right) - \sqrt{P_1^{(i)} P_2^{(i)}} \sin(\phi_1 - \phi_2).

If the two input powers are equal (:math:`P_1^{(i)} = P_2^{(i)} = P_0`) with relative phase
:math:`\Delta \phi = \phi_1 - \phi_2`:

.. math::

   P_1^{(o)} = P_0 \big(1 + \sin \Delta \phi\big), \qquad
   P_2^{(o)} = P_0 \big(1 - \sin \Delta \phi\big).

* When :math:`\Delta \phi = +\pi/2`: :math:`P_1^{(o)} = 2 P_0` (all light exits port 1) and :math:`P_2^{(o)} = 0`.
* When :math:`\Delta \phi = -\pi/2`: :math:`P_1^{(o)} = 0` and :math:`P_2^{(o)} = 2 P_0` (all light exits port 2).
* Total power is conserved at every phase: :math:`P_1^{(o)} + P_2^{(o)} = 2 P_0 = P_1^{(i)} + P_2^{(i)}`.


2. Incoherent Power Formulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.1 Mutual Incoherence and Time Averaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the input beams originate from independent, uncorrelated sources, or when
their frequency difference exceeds the detector integration bandwidth, the relative
optical phases fluctuate randomly over time:

.. math::

   \left\langle e^{j(\phi_m(t) - \phi_k(t))} \right\rangle = 0 \quad \text{for } m \neq k,

where :math:`\langle \cdot \rangle` denotes statistical / time averaging. Under this
condition, the cross-interference terms in Eq. :eq:`eq-coherent-power-complete`
average strictly to zero:

.. math::
   :label: eq-incoherent-power

   P_\ell^{(o)} = \left\langle |U_\ell^{(o)}(t)|^2 \right\rangle = \sum_{m=1}^M |T_{\ell m}|^2 P_m^{(i)}.

This is Equation (23.1-3) of Saleh & Teich.


2.2 Power (Intensity) Transfer Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defining the input power vector :math:`\mathbf{P}^{(i)} = [P_1^{(i)}, \dots, P_M^{(i)}]^T`
and output power vector :math:`\mathbf{P}^{(o)} = [P_1^{(o)}, \dots, P_N^{(o)}]^T`, the
incoherent mapping is:

.. math::
   :label: eq-power-transfer-matrix

   \mathbf{P}^{(o)} = \mathbf{S} \mathbf{P}^{(i)},

where :math:`\mathbf{S}` is the real, non-negative :math:`N \times M` **power transfer matrix**:

.. math::

   S_{\ell m} = |T_{\ell m}|^2 \ge 0.

For an ideal 2 × 2 3-dB coupler:

.. math::

   \mathbf{S} = \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{bmatrix} \implies
   \begin{bmatrix} P_1^{(o)} \\ P_2^{(o)} \end{bmatrix} =
   \begin{bmatrix} \frac{1}{2}(P_1^{(i)} + P_2^{(i)}) \\ \frac{1}{2}(P_1^{(i)} + P_2^{(i)}) \end{bmatrix}.

Regardless of the relative phases or internal phase delays, mutually incoherent inputs
always split evenly across the output ports.


3. Unified Formulation: Mutual Coherence Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To describe fields with arbitrary spatial and temporal coherence, we use the
second-order **mutual coherence matrix** (or spatial cross-spectral density matrix).

3.1 Coherence Matrix Definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The mutual spatial coherence among the :math:`M` input ports is captured by the
matrix :math:`\mathbf{J}^{(i)} \in \mathbb{C}^{M \times M}`:

.. math::

   \mathbf{J}^{(i)} \equiv \left\langle \mathbf{U}^{(i)} \mathbf{U}^{(i)\dagger} \right\rangle, \qquad
   J_{mn}^{(i)} = \left\langle U_m^{(i)} U_n^{(i)*} \right\rangle,

where :math:`\dagger` denotes the Hermitian conjugate (transpose conjugate).

* The diagonal entries are the optical powers: :math:`J_{mm}^{(i)} = \langle |U_m^{(i)}|^2 \rangle = P_m^{(i)}`.
* The off-diagonal entries represent mutual correlation:

  .. math::

     J_{mn}^{(i)} = \sqrt{P_m^{(i)} P_n^{(i)}} \, \gamma_{mn}^{(i)},

  where :math:`\gamma_{mn}^{(i)}` is the complex degree of spatial coherence between
  ports :math:`m` and :math:`n` (:math:`0 \le |\gamma_{mn}^{(i)}| \le 1`).


3.2 Transformation through the Linear Interconnect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Applying the linear field transformation :math:`\mathbf{U}^{(o)} = \mathbf{T} \mathbf{U}^{(i)}`:

.. math::

   \mathbf{J}^{(o)} = \left\langle \mathbf{U}^{(o)} \mathbf{U}^{(o)\dagger} \right\rangle
   = \left\langle (\mathbf{T} \mathbf{U}^{(i)}) (\mathbf{T} \mathbf{U}^{(i)})^\dagger \right\rangle
   = \mathbf{T} \left\langle \mathbf{U}^{(i)} \mathbf{U}^{(i)\dagger} \right\rangle \mathbf{T}^\dagger.

.. math::
   :label: eq-coherence-transformation

   \boxed{\mathbf{J}^{(o)} = \mathbf{T} \mathbf{J}^{(i)} \mathbf{T}^\dagger.}

The output power at port :math:`\ell` is simply the :math:`\ell`-th diagonal element of
:math:`\mathbf{J}^{(o)}`:

.. math::

   P_\ell^{(o)} = J_{\ell \ell}^{(o)} = \left[ \mathbf{T} \mathbf{J}^{(i)} \mathbf{T}^\dagger \right]_{\ell \ell}
   = \sum_{m=1}^M \sum_{n=1}^M T_{\ell m} T_{\ell n}^* J_{mn}^{(i)}.

Expanding this in terms of :math:`\gamma_{mn}^{(i)}`:

.. math::
   :label: eq-general-power-master

   \boxed{P_\ell^{(o)} = \sum_{m=1}^M |T_{\ell m}|^2 P_m^{(i)} + 2 \sum_{m < n}^M |T_{\ell m}| |T_{\ell n}| \sqrt{P_m^{(i)} P_n^{(i)}} \, \mathrm{Re}\Big( \gamma_{mn}^{(i)} e^{j(\theta_{\ell m} - \theta_{\ell n})} \Big)}


3.3 Limiting Cases of the Master Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Fully Coherent Inputs** (:math:`|\gamma_{mn}^{(i)}| = 1`):
   Here :math:`\gamma_{mn}^{(i)} = e^{j(\phi_m - \phi_n)}`, and the matrix :math:`\mathbf{J}^{(i)}`
   has rank 1:

   .. math::

      \mathbf{J}^{(i)} = \mathbf{U}^{(i)} \mathbf{U}^{(i)\dagger}.

   Equation :eq:`eq-general-power-master` exactly reproduces the coherent interference
   expansion in Eq. :eq:`eq-coherent-power-complete`.

2. **Mutually Incoherent Inputs** (:math:`\gamma_{mn}^{(i)} = \delta_{mn}`):
   The off-diagonal terms vanish, and :math:`\mathbf{J}^{(i)}` becomes purely diagonal:

   .. math::

      \mathbf{J}^{(i)} = \operatorname{diag}\left( P_1^{(i)}, P_2^{(i)}, \dots, P_M^{(i)} \right).

   Equation :eq:`eq-general-power-master` collapses to Eq. (23.1-3):

   .. math::

      P_\ell^{(o)} = \sum_{m=1}^M |T_{\ell m}|^2 P_m^{(i)}.

3. **Partially Coherent Inputs** (:math:`0 < |\gamma_{mn}^{(i)}| < 1`):
   Interference fringes persist, but their visibility (contrast) is scaled by
   :math:`|\gamma_{mn}^{(i)}|`.


4. Energy Conservation and Mathematical Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.1 Lossless Interconnects: Unitarity of Matrix T
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For an :math:`N \times N` coupler without dissipation, scattering, or radiation loss,
the total output power must equal the total input power for **any** arbitrary input
field state :math:`\mathbf{U}^{(i)}`:

.. math::

   P_{\mathrm{total}}^{(o)} = \mathbf{U}^{(o)\dagger} \mathbf{U}^{(o)} = \mathbf{U}^{(i)\dagger} (\mathbf{T}^\dagger \mathbf{T}) \mathbf{U}^{(i)} = \mathbf{U}^{(i)\dagger} \mathbf{U}^{(i)} = P_{\mathrm{total}}^{(i)}.

This condition holds for all :math:`\mathbf{U}^{(i)}` if and only if :math:`\mathbf{T}` is a **unitary matrix**:

.. math::
   :label: eq-unitarity

   \mathbf{T}^\dagger \mathbf{T} = \mathbf{I} \quad \text{and} \quad \mathbf{T} \mathbf{T}^\dagger = \mathbf{I}.

In terms of elements:

* **Column orthonormality** (conservation from input ports):

  .. math::

     \sum_{\ell=1}^N T_{\ell m} T_{\ell k}^* = \delta_{mk}.

* **Row orthonormality** (conservation to output ports):

  .. math::

     \sum_{m=1}^N T_{\ell m} T_{k m}^* = \delta_{\ell k}.


4.2 Orthostochasticity of Power Transfer Matrix S
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Evaluating the column and row conditions for :math:`m = k` and :math:`\ell = k`:

.. math::

   \sum_{\ell=1}^N |T_{\ell m}|^2 = \sum_{\ell=1}^N S_{\ell m} = 1 \quad (\forall m), \qquad
   \sum_{m=1}^N |T_{\ell m}|^2 = \sum_{m=1}^N S_{\ell m} = 1 \quad (\forall \ell).

Therefore:

* Every column sums to 1 (all power injected into input :math:`m` is distributed among outputs).
* Every row sums to 1.

A non-negative matrix whose rows and columns both sum to 1 is called **doubly stochastic**
(or bistochastic). A matrix whose elements are the squared moduli of a unitary matrix
(:math:`S_{\ell m} = |T_{\ell m}|^2`) is specifically known as an **orthostochastic matrix**.


4.3 Lossy Couplers and Singular Value Limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Real couplers exhibit excess loss and finite port isolation. For passive lossy systems:

* The eigenvalues of :math:`\mathbf{T}^\dagger \mathbf{T}` are bounded: :math:`0 \le \lambda_j(\mathbf{T}^\dagger \mathbf{T}) \le 1`.
* The singular values of :math:`\mathbf{T}` satisfy :math:`\sigma_j(\mathbf{T}) \le 1`.
* The column sums of :math:`\mathbf{S}` satisfy :math:`\sum_{\ell=1}^N S_{\ell m} \le 1`.


5. Coupler Performance Specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In optical engineering, practical multi-port couplers and switches are specified by
standard logarithmic power ratios:

* **Insertion Loss (IL)** between input port :math:`m` and output port :math:`\ell`:

  .. math::

     \mathrm{IL}_{\ell m} = -10 \log_{10}\left( \frac{P_\ell^{(o)}}{P_m^{(i)}} \right) = -10 \log_{10}|T_{\ell m}|^2 = -10 \log_{10} S_{\ell m} \quad [\mathrm{dB}].

* **Splitting Ratio** for port :math:`\ell`:

  .. math::

     \mathrm{SR}_\ell = \frac{P_\ell^{(o)}}{\sum_{k=1}^N P_k^{(o)}} = \frac{S_{\ell m}}{\sum_{k=1}^N S_{k m}}.

* **Excess Loss (EL)** of the device when driven by port :math:`m`:

  .. math::

     \mathrm{EL}_m = -10 \log_{10}\left( \frac{\sum_{\ell=1}^N P_\ell^{(o)}}{P_m^{(i)}} \right) = -10 \log_{10}\left( \sum_{\ell=1}^N S_{\ell m} \right) \quad [\mathrm{dB}].

* **Crosstalk / Isolation** between unintended output port :math:`\ell` and intended output port :math:`k`:

  .. math::

     \mathrm{XT}_{\ell k} = 10 \log_{10}\left( \frac{P_\ell^{(o)}}{P_k^{(o)}} \right) \quad [\mathrm{dB}].


6. Summary Comparison Table
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: Comparison of Coherent, Incoherent, and Partially Coherent Regimes
   :widths: 22 26 26 26
   :header-rows: 1

   * - Characteristic
     - Coherent Regime (Eq. 23.1-1)
     - Incoherent Regime (Eq. 23.1-3)
     - General / Partially Coherent
   * - **Primary Variable**
     - Field vector :math:`\mathbf{U} \in \mathbb{C}^N`
     - Power vector :math:`\mathbf{P} \in \mathbb{R}^N`
     - Coherence matrix :math:`\mathbf{J} \in \mathbb{C}^{N \times N}`
   * - **Governing Relation**
     - :math:`\mathbf{U}^{(o)} = \mathbf{T} \mathbf{U}^{(i)}`
     - :math:`\mathbf{P}^{(o)} = \mathbf{S} \mathbf{P}^{(i)}`
     - :math:`\mathbf{J}^{(o)} = \mathbf{T} \mathbf{J}^{(i)} \mathbf{T}^\dagger`
   * - **Matrix Nature**
     - Complex :math:`\mathbf{T}` (unitary if lossless)
     - Real :math:`S_{\ell m} = |T_{\ell m}|^2` (orthostochastic)
     - Bilinear transformation with :math:`\mathbf{T}, \mathbf{T}^\dagger`
   * - **Output Power**
     - :math:`|\sum_m T_{\ell m} U_m^{(i)}|^2`
     - :math:`\sum_m |T_{\ell m}|^2 P_m^{(i)}`
     - :math:`[\mathbf{T} \mathbf{J}^{(i)} \mathbf{T}^\dagger]_{\ell\ell}`
   * - **Phase Dependence**
     - Fully sensitive to relative source & device phases
     - Insensitive to optical phases
     - Scaled by degree of coherence :math:`|\gamma_{mn}|`
   * - **Interference Terms**
     - Present (:math:`\propto 2 \sqrt{P_m P_k} \cos \Delta \Phi`)
     - Strictly zero
     - Scaled (:math:`\propto 2 \sqrt{P_m P_k} |\gamma| \cos \Delta \Phi`)

In-text exercises
-----------------

Exercise 23.1-1 — Interconnection capacity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Definitions and setup.**  The exercise asks for an upper bound on
the number of independently resolvable input-to-output connections, not just
the number of rays that can be drawn.  Use the segmented hologram of textbook
Fig. 23.1-6: each incoming beam illuminates its own grating region, and the
spatial frequencies recorded in that region select its outgoing directions.
The notation resets for this exercise: :math:`L` counts inputs and
:math:`M` counts directions per input, unlike the preceding matrix section's
use of :math:`M` for the number of inputs.

* :math:`a` is the side length of the whole square hologram, in mm.
* :math:`B` is its printable spatial-frequency limit, in lines/mm.  We use
  the exercise's bandwidth convention, for which the full hologram has
  space-bandwidth product :math:`(Ba)^2`.
* :math:`L` is the number of incoming beams, hence the number of independently
  illuminated regions sharing the total area :math:`a^2`.
* :math:`M` is the number of resolvable outgoing directions **per incoming
  beam**.  There are therefore :math:`ML` input-to-output connections.

For an equal-area division, one beam gets a rectangular region of width
:math:`w_x` and height :math:`w_y`, with :math:`w_xw_y=a^2/L`.  These are
dimensions of a grating region, not the distance to the output screen.

.. _fop-exercise-23-1-1-illustration:

.. figure:: /_static/knowledge_base/worked_exercises/fundamentals_of_photonics/exercise_illustrations/exercise_23_01_01.svg
   :alt: A hologram divided among four input beams, and the spatial-frequency grid of resolvable outgoing directions for one region
   :align: center
   :width: 95%

   **Figure 129 — Exercise 23.1-1: Interconnection capacity.**  In the
   example :math:`L=4`, each beam illuminates a square of side :math:`a/2`.
   Its finite size sets frequency spacings :math:`1/w_x` and :math:`1/w_y`;
   the available two-dimensional frequency range holds at most
   :math:`B^2w_xw_y=(Ba)^2/4` resolvable directions for that beam.

**Step 2 — Mathematical formulas used.**  A finite rectangular aperture has
a sinc-shaped angular spectrum, by the :ref:`Fourier-transform relation
<fop-formula-fourier>`.  Its width gives the spatial-frequency resolution.
Counting resolvable directions then requires only
:ref:`algebra and dimensional checks <fop-formula-algebra>`, not a
stationary-value calculation.  This is the spatial analogue of the
time-duration/frequency-resolution argument in textbook Sec. 19.2C,
Eq. (19.2-9), which the exercise gives as a hint.

**Step 3 — Worked derivation.**

**Why does region size limit the number of directions?**  A grating with
spatial frequency :math:`\nu_x` deflects a paraxial beam through an angle
:math:`\theta_x\simeq\lambda\nu_x`, where :math:`\lambda` is the optical
wavelength.  But a beam passing through a region of width :math:`w_x` does
not emerge as an infinitely narrow ray: diffraction gives an angular width
of order :math:`\lambda/w_x`.  Two grating frequencies must consequently
differ by about :math:`1/w_x` to give resolvable directions.  The same
argument applies along :math:`y`:

.. math::
   :label: fop-exercise-23-1-1-frequency-resolution

   \delta\nu_x\simeq\frac{1}{w_x},\qquad
   \delta\nu_y\simeq\frac{1}{w_y}.

More explicitly, truncating a sinusoidal grating to width :math:`w_x`
changes its sharp spatial-frequency peak at :math:`\nu_{x0}` into a factor
:math:`\operatorname{sinc}[w_x(\nu_x-\nu_{x0})]`, where
:math:`\operatorname{sinc}(u)=\sin(\pi u)/(\pi u)`.  Its first zeros are
:math:`1/w_x` from the peak.  This is the missing physical reason that
different written frequencies cannot be packed arbitrarily close together.

**Count the directions available to one input.**  Within the bandwidth
:math:`B`, the region resolves about :math:`B/\delta\nu_x=Bw_x` directions
along :math:`x` and :math:`B/\delta\nu_y=Bw_y` along :math:`y`.
An outgoing direction is a pair of these frequency coordinates, so the
two counts multiply.  Using the ideal space-bandwidth counting convention
specified in the exercise gives

.. math::
   :label: fop-exercise-23-1-1-directions-per-input

   M\leq(Bw_x)(Bw_y)
     =B^2w_xw_y
     =\frac{B^2a^2}{L}.

**Now count all input-to-output connections.**  Multiplying by the
:math:`L` inputs gives the requested capacity bound:

.. math::
   :label: fop-exercise-23-1-1-capacity

   \boxed{ML\leq B^2a^2=(Ba)^2}.

Thus :math:`L` and :math:`M` are not independent capacities: adding inputs
divides the same hologram area into smaller regions, which broadens each
diffracted spot and reduces the number of resolvable directions per input.
For unequal regions of areas :math:`A_\ell`, the same reasoning gives
:math:`M_\ell\leq B^2A_\ell`; summing over the nonoverlapping regions again
limits the total number of connections to :math:`B^2a^2`.

**Convert capacity into a density.**  If every one of the :math:`L` inputs
connects to every one of the :math:`M` output points, the number of links is
:math:`ML`, not :math:`M+L`.  Divide by the hologram area:

.. math::
   :label: fop-exercise-23-1-1-link-density

   \frac{ML}{a^2}\leq B^2
     =(1000\ \mathrm{mm}^{-1})^2
     =10^6\ \mathrm{interconnections/mm^2}.

The essential chain is :math:`w_xw_y=a^2/L`, then
:math:`M\leq(Bw_x)(Bw_y)=B^2a^2/L`, hence :math:`ML\leq(Ba)^2`.
This is an ideal resolution-based upper bound, not a guarantee that a real
hologram attains it.  Diffraction efficiency, crosstalk, numerical aperture,
and a stricter spot-separation criterion can reduce the usable count.

**Step 4 — State the numbered result.**  The total connection count and its
maximum density in the exercise's model are

.. math::
   :label: fop-exercise-23-1-1-result

   \boxed{ML\leq(Ba)^2,\qquad
   \left(\frac{ML}{a^2}\right)_{\max}
   =B^2=10^6\ \mathrm{interconnections/mm^2}}.


**Step 5 — Check.**  The product :math:`Ba` is dimensionless, as a direction
count must be, whereas :math:`B^2` has units :math:`\mathrm{mm}^{-2}`.
For :math:`L=1`, one input uses the whole aperture and can access at most
:math:`(Ba)^2` directions.  For four equal square regions, each side is
halved, the frequency spacing doubles in both coordinates, and each input
gets only :math:`(Ba)^2/4` directions: multiplying by four recovers the same
total.  For a numerical check, :math:`a=1\ \mathrm{mm}`, :math:`L=100`, and
:math:`B=1000\ \mathrm{mm}^{-1}` give
:math:`w_x=w_y=0.1\ \mathrm{mm}` and :math:`\delta\nu_x=\delta\nu_y=
10\ \mathrm{mm}^{-1}`.  There are at most :math:`100\times100=10^4`
directions per input, hence :math:`100\times10^4=10^6` links in total.

Exercise 23.1-2 — Separable logarithmic map
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

.. _fop-exercise-23-1-2-illustration:

.. figure:: /_static/knowledge_base/worked_exercises/fundamentals_of_photonics/exercise_illustrations/exercise_23_01_02.svg
   :alt: Illustrated calculation map for Exercise 23.1-2, Separable logarithmic map
   :align: center
   :width: 95%

   **Figure 130 — Exercise 23.1-2: Separable logarithmic map.** The
   diagram identifies the input quantities, physical operation, requested
   result, variable meanings, and an independent verification route. Every
   symbol in the variable strip is labeled on the model itself.

**Step 2 — Mathematical formulas used.**  The working uses :ref:`product, quotient, and chain rules <fop-formula-product-chain>`, :ref:`exponential, logarithmic, and phasor identities <fop-formula-exponentials>`, and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Step 3 — Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

Differentiate the proposed phase:

.. math::
   :label: fop-exercise-23-1-2-eq-1

   {\partial\phi\over\partial x}={2\pi\over\lambda d}(\ln x-x),\qquad
   {\partial\phi\over\partial y}={2\pi\over\lambda d}(\ln y-y).

Equation (23.1-7) then gives :math:`x'=x+(\lambda d/2\pi)\phi_x=\ln x`
and likewise :math:`y'=\ln y`, which proves the map.

**Step 4 — Interpret the result.**  The final relation or conclusion in Step 3 is the requested result.  Read its sign, scale, or physical classification using the conventions fixed in Step 1.

**Step 5 — Check.**  Equation :eq:`fop-exercise-23-1-2-eq-1` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.

Exercise 23.4-1 — Bistable nonlinearities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1 — Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

.. _fop-exercise-23-4-1-illustration:

.. figure:: /_static/knowledge_base/worked_exercises/fundamentals_of_photonics/exercise_illustrations/exercise_23_04_01.svg
   :alt: Illustrated calculation map for Exercise 23.4-1, Bistable nonlinearities
   :align: center
   :width: 95%

   **Figure 131 — Exercise 23.4-1: Bistable nonlinearities.** The
   diagram identifies the input quantities, physical operation, requested
   result, variable meanings, and an independent verification route. Every
   symbol in the variable strip is labeled on the model itself.

**Step 2 — Mathematical formulas used.**  The working uses :ref:`stationary-value condition <fop-formula-stationary>`, :ref:`product, quotient, and chain rules <fop-formula-product-chain>`, and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Step 3 — Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

For each candidate plot :math:`y(x)=x/\eta(x)` and locate folds from
:math:`dy/dx=0`; two folds delimit a three-valued output interval.  Working
choices are (a) :math:`a=0.2`, (b) :math:`a=5,\theta=0`, (c)
:math:`\theta=0`, (d) :math:`a=0.5`, and (e) :math:`a=10`.  For example,
case (e) has
:math:`y=x(x+a)^2/(x+1)^2` and its stationary numerator is
:math:`x^2+(3-a)x+a`; at :math:`a=10` the folds are exactly
:math:`\boxed{x=2,5}`.  The same derivative test, rather than visual guesswork,
verifies the other four plots.

**Step 4 — State the numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-exercise-23-4-1-result

   \boxed{x=2,5}


**Step 5 — Check.**  Equation :eq:`fop-exercise-23-4-1-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.

End-of-chapter problems
-----------------------

Problem 23.1-3 — Conformal-map hologram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`product, quotient, and chain rules <fop-formula-product-chain>`, :ref:`vector-calculus identities <fop-formula-vector-calculus>`, and :ref:`exponential, logarithmic, and phasor identities <fop-formula-exponentials>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

For a single continuous phase mask, Eq. (23.1-7) would require
:math:`\phi_x\propto\ln r-x` and :math:`\phi_y\propto\tan^{-1}(y/x)-y`.
But

.. math::
   :label: fop-problem-23-1-3-eq-1

   \partial_y(\ln r-x)={y\over r^2},\qquad
   \partial_x[\tan^{-1}(y/x)-y]=-{y\over r^2}.

The mixed derivatives disagree, so :math:`\boxed{\text{no scalar phase
function exists for this map in one thin hologram}}`.  It requires at least a
two-element coordinate transformer (or a segmented/nonlocal implementation);
the curl test is the essential design result.

**Check.**  Equation :eq:`fop-problem-23-1-3-eq-1` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.

Problem 23.2-1 — Four-channel cascaded MZIs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

Near :math:`\lambda_0`, :math:`\Delta\nu=c\Delta\lambda/\lambda_0^2=
24.96` GHz.  Adjacent channels must swap ports in the first MZI, so
:math:`\Delta d=c/(2n\Delta\nu)=\boxed{2.612\ \mathrm{mm}}`.  Each second-
stage MZI separates channels spaced by :math:`2\Delta\nu`, so both use
:math:`\boxed{1.306\ \mathrm{mm}}`.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-2-1-result

   \boxed{1.306\ \mathrm{mm}}


**Check.**  Equation :eq:`fop-problem-23-2-1-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.  Repeat the substitution with unrounded intermediate values and retain the displayed units; the final unit must have the requested dimension.

Problem 23.2-2 — WGR wavelength increment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`optical path and Fermat's principle <fop-formula-fermat>` and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

Adjacent WGR outputs require an optical path increment equal to the channel
spacing: :math:`n\Delta d_b=\Delta\lambda`.  Hence
:math:`\boxed{\Delta d_b=0.2\ \mathrm{nm}/2.3=0.08696\ \mathrm{nm}}` in the
star-coupler material.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-2-2-result

   \boxed{\Delta d_b=0.2\ \mathrm{nm}/2.3=0.08696\ \mathrm{nm}}


**Check.**  Equation :eq:`fop-problem-23-2-2-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.  Repeat the substitution with unrounded intermediate values and retain the displayed units; the final unit must have the requested dimension.

Problem 23.2-3 — Two-by-two wavelength transpose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

An :math:`l\to m` path transmits wavelength :math:`\lambda` when
:math:`n\Delta d_{lm}=q_{lm}\lambda` for an integer order, while the rejected
wavelength is not an integer divisor.  Choose
:math:`\Delta d_{11}` resonant for :math:`\lambda_1`,
:math:`\Delta d_{12}` for :math:`\lambda_2`,
:math:`\Delta d_{21}` for :math:`\lambda_3`, and
:math:`\Delta d_{22}` for :math:`\lambda_4`; explicitly
:math:`\boxed{n\Delta d_{11}=q_1\lambda_1,
n\Delta d_{12}=q_2\lambda_2,n\Delta d_{21}=q_3\lambda_3,
n\Delta d_{22}=q_4\lambda_4}`.  Selecting integers that make every unwanted
ratio nonintegral completes the router.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-2-3-result

   \boxed{n\Delta d_{11}=q_1\lambda_1,
   n\Delta d_{12}=q_2\lambda_2,n\Delta d_{21}=q_3\lambda_3,
   n\Delta d_{22}=q_4\lambda_4}


**Check.**  Equation :eq:`fop-problem-23-2-3-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.

Problem 23.3-1 — Cascaded-switch loss and crosstalk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`power and decibel conversions <fop-formula-power-decibels>` and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

The worst route through the five-element 4-by-4 network traverses three
2-by-2 switches, so loss is :math:`\boxed{3(0.5)=1.5\ \mathrm{dB}}`.  Adding
three independent :math:`10^{-3}` leakage powers gives crosstalk
:math:`10\log_{10}(3\times10^{-3})=\boxed{-25.2\ \mathrm{dB}}`; a deliberately
conservative coherent phase alignment would instead bound it at -20.5 dB.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-3-1-result

   10\log_{10}(3\times10^{-3})=\boxed{-25.2\ \mathrm{dB}}


**Check.**  Equation :eq:`fop-problem-23-3-1-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Converting the final decibel value back to a linear power ratio checks the logarithm, sign, and accumulated loss budget.  Repeat the substitution with unrounded intermediate values and retain the displayed units; the final unit must have the requested dimension.

Problem 23.3-2 — MZI voltage-error crosstalk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`power and decibel conversions <fop-formula-power-decibels>`, :ref:`trigonometric and small-angle identities <fop-formula-trigonometry>`, and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

The cross state needs :math:`\boxed{V=V_\pi}`.  A 1% error leaves fractional
leakage ratio :math:`\tan^2(0.01\pi/2)=2.468\times10^{-4}`, hence
:math:`\boxed{XT=-36.08\ \mathrm{dB}}`.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-3-2-result

   \boxed{XT=-36.08\ \mathrm{dB}}


**Check.**  Equation :eq:`fop-problem-23-3-2-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Converting the final decibel value back to a linear power ratio checks the logarithm, sign, and accumulated loss budget.  Repeat the substitution with unrounded intermediate values and retain the displayed units; the final unit must have the requested dimension.

Problem 23.3-3 — TSI with programmable delays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

Demultiplex the incoming frame into :math:`N` spatial lanes.  Program lane
:math:`i` with delay :math:`d_i=(\pi(i)-i)\bmod N` slots for the requested
permutation :math:`\pi`; a second bank adds a common frame delay so all values
are causal.  Remultiplex lanes in their fixed order.  This
:math:`\boxed{\text{DEMUX}\to\text{programmable delays}\to\text{MUX}}`
construction absorbs the original fixed-delay/space-switch/fixed-delay stages
into the addressable delay settings.

**Numbered result.**  The principal result obtained in the working is

.. math::
   :label: fop-problem-23-3-3-result

   \boxed{\text{DEMUX}\to\text{programmable delays}\to\text{MUX}}


**Check.**  Equation :eq:`fop-problem-23-3-3-result` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  Check that dimensions agree term by term, then test the simplest symmetry or limiting case for the expected sign and scale.

Problem 23.4-2 — Threshold optical logic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses the physical definitions stated in the item; no separate calculus or algebraic identity is required for this qualitative comparison.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

Sum equal optical inputs and choose a threshold between levels: between one
and two units gives AND, while between zero and one gives OR.  Complement the
threshold device's output (or exchange bright/dark ports) for NAND and NOR.
One scalar threshold cannot implement XOR because its truth set is not
linearly separable; use an OR followed by suppression of the two-input level,
or two threshold stages.  The same sum with threshold :math:`0.5` implements
OR for any :math:`N`.

**Check.**  For a qualitative conclusion, test every absolute statement against the stated assumptions and at least one limiting case or counterexample.

Problem 23.4-3 — Kerr-feedback interferometer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Definitions and setup.**  Symbols are local to this item and follow the chapter convention.  Each physical quantity and supplied numerical value is introduced at its first use below; angles are in radians unless a degree symbol is shown, and units are retained through numerical substitution.

**Mathematical formulas used.**  The working uses :ref:`stationary-value condition <fop-formula-stationary>`, :ref:`trigonometric and small-angle identities <fop-formula-trigonometry>`, and :ref:`algebraic rearrangement and dimensional checks <fop-formula-algebra>`.

**Worked derivation.**  The calculation is kept in symbolic form until the governing relation has been rearranged for the requested quantity.

The Kerr arm phase is :math:`\Delta\phi=\pi I_o/I_\pi+\phi`, so MZI
interference gives
:math:`\boxed{I_o/I_i=[1+\cos(\pi I_o/I_\pi+\phi)]/2}`.  For :math:`\phi=0`,
write :math:`x=I_o/I_\pi` and
:math:`y=I_i/I_\pi=2x/[1+\cos(\pi x)]`.  Then

.. math::
   :label: fop-problem-23-4-3-eq-1

   {dI_o\over dI_i}=
   \left\{{2\over1+\cos\pi x}+{2\pi x\sin\pi x\over(1+\cos\pi x)^2}\right\}^{-1}.

The ideal differential gain diverges at fold points where the denominator
vanishes; physical loss and finite response time cap that formal maximum.

**Check.**  Equation :eq:`fop-problem-23-4-3-eq-1` can be checked by substituting it back into the preceding governing relation and reversing the algebraic steps.  The zero-angle or paraxial limit supplies an independent sign and magnitude check whenever that limit is part of the model.
