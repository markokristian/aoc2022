use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};

fn part1() {
    let file = File::open("./input/02").expect("Can't open file");
    let reader = io::BufReader::new(file);
    let mapping = HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 1), ("Y", 2), ("Z", 3)]);
    let outcomes = HashMap::from([(-1, 0), (2, 0), (-2, 6), (1, 6)]);
    let mut score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let round = line.split(' ').collect::<Vec<&str>>();
        let opp = mapping.get(round[0]).copied().unwrap();
        let me = mapping.get(round[1]).copied().unwrap();
        score += me + {
            if opp == me {
                3i32
            } else {
                let diff = me - opp;
                outcomes.get(&diff).copied().unwrap()
            }
        }
    }
    println!("{}", score);
}

fn part2() {
    let file = File::open("./input/02").expect("Can't open file");
    let reader = io::BufReader::new(file);
    let mapping = HashMap::from([("A", 1), ("B", 2), ("C", 3), ("X", 0), ("Y", 3), ("Z", 6)]);
    let outcomes = HashMap::from([
        (1, HashMap::from([(6, 2), (0, 3), (3, 1)])),
        (2, HashMap::from([(0, 1), (6, 3), (3, 2)])),
        (3, HashMap::from([(6, 1), (0, 2), (3, 3)])),
    ]);
    let mut score = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let round = line.split(' ').collect::<Vec<&str>>();
        let opp = mapping.get(round[0]).copied().unwrap();
        let outcome = mapping.get(round[1]).copied().unwrap();
        let me = outcomes
            .get(&opp)
            .and_then(|o| o.get(&outcome))
            .copied()
            .unwrap();
        score += me + outcome;
    }
    println!("{}", score);
}

fn main() {
    part1();
    part2()
}
