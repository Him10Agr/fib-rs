use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

///#[pyfunction]
//fn say_hello() -> PyResult<()> {
//    println!("Saying hello from Rust!");
//    return Ok(());
//}

//#[pymodule]
//fn fib_rs(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
//    m.add_function(wrap_pyfunction!(say_hello,_py)?)?;
//    return Ok(());
//}

#[pyfunction]
fn say_hello(){
    println!("Saying hello from Rust!!");
}

#[pymodule]
fn fib_rs(_py: Python, m: &Bound<'_,PyModule>) -> PyResult<()> {
    let _ = m.add_wrapped(wrap_pyfunction!(say_hello));
    return Ok(());
}