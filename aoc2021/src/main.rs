use std::time::Instant;

mod aoc01;
mod aoc02;

fn main() {
    let start = Instant::now();

    aoc01::part1();
    aoc01::part2();
    aoc02::part1();
    aoc02::part2();

    println!("Total runtime: {:?}", Instant::now() - start);
}
