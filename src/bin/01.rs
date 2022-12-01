use priority_queue::PriorityQueue;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let Ok(lines) = read_lines("./input/01") else { return };
    let mut pq: PriorityQueue<i32, i32> = PriorityQueue::new();
    let mut sum: i32 = 0;
    for line in lines.map(|l| l.unwrap()) {
        if line.is_empty() {
            pq.push(sum, sum);
            sum = 0;
            continue;
        }
        sum += line.parse::<i32>().unwrap();
    }
    let sum: i32 = pq.into_sorted_iter().take(3).map(|e| e.0).sum();
    print!("{}", sum);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
