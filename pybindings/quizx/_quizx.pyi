# Type stubs for the Rust bindings

from typing import final
from builtins import complex as complex_

@final
class Scalar:
    @staticmethod
    def complex(complex: complex_) -> Scalar: ...
    @staticmethod
    def real(real: float) -> Scalar: ...
    @staticmethod
    def from_phase(phase: float) -> Scalar: ...
    @staticmethod
    def from_int_coeffs(coeffs: list[int]) -> Scalar: ...
    @staticmethod
    def one_plus_phase(phase: float) -> Scalar: ...
    @staticmethod
    def sqrt2_pow(n: int) -> Scalar: ...
    def complex_value(self) -> complex_: ...
    def mul_sqrt2_pow(self, n: int) -> Scalar: ...
    def mul_phase(self, phase: float) -> Scalar: ...
    @staticmethod
    def zero() -> Scalar: ...
    @staticmethod
    def one() -> Scalar: ...
    def is_zero(self) -> bool: ...
    def is_one(self) -> bool: ...
    def conjugate(self) -> Scalar: ...

@final
class VecGraph:
    scalar: Scalar
    def vindex(self) -> int: ...
    def neighbor_at(self, v: int, n: int) -> int: ...
    def num_vertices(self) -> int: ...
    def num_edges(self) -> int: ...
    def add_vertex(
        self, ty_num: int, qubit: int, row: int, phase: tuple[int, int]
    ) -> int: ...
    def contains_vertex(self, v: int) -> bool: ...
    def add_edge(self, e: tuple[int, int], et_num: int) -> None: ...
    def add_edge_smart(self, e: tuple[int, int], et_num: int) -> None: ...
    def remove_vertex(self, v: int) -> None: ...
    def remove_edge(self, e: tuple[int, int]) -> None: ...
    def degree(self, v: int) -> int: ...
    def connected(self, s: int, t: int) -> bool: ...
    def vertex_type(self, v: int) -> int: ...
    def set_vertex_type(self, v: int, ty_num: int) -> None: ...
    def edge_type(self, e: tuple[int, int]) -> int: ...
    def set_edge_type(self, e: tuple[int, int], et_num: int) -> None: ...
    def phase(self, v: int) -> tuple[int, int]: ...
    def set_phase(self, v: int, phase: tuple[int, int]) -> None: ...
    def add_to_phase(self, v: int, phase: tuple[int, int]) -> None: ...
    def qubit(self, v: int) -> int: ...
    def set_qubit(self, v: int, q: int) -> None: ...
    def row(self, v: int) -> int: ...
    def set_row(self, v: int, r: int) -> None: ...
    def inputs(self) -> list[int]: ...
    def num_inputs(self) -> int: ...
    def set_inputs(self, inputs: list[int]) -> None: ...
    def outputs(self) -> list[int]: ...
    def num_outputs(self) -> int: ...
    def set_outputs(self, outputs: list[int]) -> None: ...

@final
class Circuit:
    @staticmethod
    def from_qasm(qasm: str) -> Circuit: ...
    @staticmethod
    def load(file: str) -> Circuit: ...
    def to_qasm(self) -> str: ...
    def to_graph(self) -> VecGraph: ...
    def num_gates(self) -> int: ...
    def stats(self) -> str: ...

@final
class CircuitStats:
    def qubits(self) -> int: ...
    def total(self) -> int: ...
    def oneq(self) -> int: ...
    def twoq(self) -> int: ...
    def moreq(self) -> int: ...
    def cliff(self) -> int: ...
    def non_cliff(self) -> int: ...
    def to_string(self) -> str: ...

@final
class Decomposer:
    scalar: Scalar
    @staticmethod
    def empty() -> Decomposer: ...
    def __init__(self, g: VecGraph) -> None: ...
    def graphs(self) -> list[VecGraph]: ...
    def apply_optimizations(self, b: bool) -> None: ...
    def max_terms(self) -> int: ...
    def decomp_top(self) -> None: ...
    def decomp_all(self) -> None: ...
    def decomp_until_depth(self, depth: int) -> None: ...

def dummy(a: int) -> str: ...
def interior_clifford_simp(g: VecGraph): ...
def clifford_simp(g: VecGraph): ...
def full_simp(g: VecGraph): ...
def extract_circuit(g: VecGraph) -> Circuit: ...
