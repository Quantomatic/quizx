// QuiZX - Rust library for quantum circuit rewriting and optimisation
//         using the ZX-calculus
// Copyright (C) 2021 - Aleks Kissinger
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

use std::time::Instant;
use std::io;
use std::io::Write;
use quizx::circuit::*;
use quizx::graph::*;
// use quizx::scalar::*;
// use quizx::tensor::*;
use quizx::vec_graph::Graph;
use quizx::decompose::Decomposer;
use rayon::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let qs = 40;
    let c = Circuit::random()
        .qubits(qs)
        .depth(400)
        .seed(1337)
        .p_t(0.25)
        .with_cliffords()
        .build();
    let mut g: Graph = c.to_graph();
    g.plug_inputs(&vec![BasisElem::Z0; qs]);
    g.plug_outputs(&vec![BasisElem::Z0; qs]);

    println!("g has T-count: {}", g.tcount());
    quizx::simplify::full_simp(&mut g);


    let time = Instant::now();
    let mut d = Decomposer::new(&g);
    d.with_full_simp();
    let max = d.max_terms();
    println!("Naive: {} terms", max);

    let n = 500;
    println!("Trying {} candidates...", n);
    let v: Vec<_> = (0..n).collect();
    let (_, ts) = v.par_iter().map(|_| {
        let mut d1 = d.clone();
        let g1 = d1.pop_graph();
        let ts1 = Decomposer::random_ts(&g1);
        d1.decomp_ts(0, g1, &ts1);
        d1.decomp_until_depth(3);
        (d1.max_terms(), ts1)
    }).min().unwrap();
    println!("done.");

    let g1 = d.pop_graph();
    d.decomp_ts(0, g1, &ts);

    // if g.tcount() > 100 { continue; }
    println!("Decomposing g with (reduced) T-count: {}", g.tcount());
    let d = d.decomp_parallel(3);
    // d.decomp_all();
    println!("Finished in {:.2?}", time.elapsed());

    println!("Got {} terms for T-count {} (naive {} terms)", d.nterms, g.tcount(), max);
    println!("{:?}", d.scalar);

    Ok(())
}
