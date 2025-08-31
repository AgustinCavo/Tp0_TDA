
use std::fs::{create_dir_all, File};
use std::io::{BufWriter, Write};
use std::time::Instant;

fn sumas_divisores_propios(max: usize) -> Vec<u64> {

    let mut sums = vec![1u64; max + 1];
    sums[0] = 0;
    sums[1] = 0;
    let half = max / 2;
    for d in 1..=half {
        let mut m = d * 2;
        while m <= max {
            sums[m] += d as u64;
            m += d;
        }
    }
    sums
}

fn amigos_a_archivo(max: usize, path: &str) -> std::io::Result<()> {
    let t0 = Instant::now();
    let sums = sumas_divisores_propios(max);
    let mut vis = vec![false; max + 1];

    let file = File::create(path)?;
    let mut w = BufWriter::new(file);

    for a in 1..=max {
        if vis[a] {
            continue;
        }
        let b = sums[a] as usize;

        if b == a {

            writeln!(w, "{} {}", a, a)?;
        } else if b >= 1 && b <= max && sums[b] as usize == a {

            if a < b {
                writeln!(w, "{} {}", a, b)?;
            }
            vis[a] = true;
            vis[b] = true;
        }
    }

    let dt = t0.elapsed().as_secs_f64();
    writeln!(w, "Tiempo: {:.6} s", dt)?;
    w.flush()?;
    Ok(())
}

fn main() -> std::io::Result<()> {

    let args = std::env::args().skip(1);
    let max_values: Vec<usize> = if args.len() > 0 {
        args.filter_map(|s| s.replace('_', "").parse::<usize>().ok()).collect()
    } else {
        vec![
            50000, 100000, 150000, 250000, 350000,
            500000, 1000000, 5000000, 10000000, 50000000, 100000000

        ]
    };

    let outdir = "corridas";
    create_dir_all(outdir)?;

    for m in max_values {
        let path = format!("{}/{}_refactor_amigos.txt", outdir, m);
        eprintln!("Procesando MAX={} -> {}", m, path);
        amigos_a_archivo(m, &path)?;
        eprintln!("OK");
    }

    Ok(())
}