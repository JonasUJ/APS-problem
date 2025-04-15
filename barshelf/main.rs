use std::io::{BufRead, stdin};

mod fenwick_tree;

fn main() {
    let mut lines = stdin().lock().lines().map(Result::unwrap);

    // Number of bottles not needed
    let _n = lines.next().unwrap().parse::<usize>().unwrap();

    // seq has list of bottles
    let seq = lines.next().unwrap();
    let seq = seq
        .split_whitespace()
        .map(|s| s.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    // Twice the height of the tallest bottle
    // The Fenwick tree needs an upper bound
    let max = *seq.iter().max().unwrap() * 2;

    // Two FenwickTrees - one for "bottles twice as tall as 'this'" and the other for "bottles
    // twice as tall as the bottles twice as tall as 'this'"
    let mut level1 = fenwick_tree::FenwickTree::new(max);
    let mut level2 = fenwick_tree::FenwickTree::new(max);

    let mut count = 0;
    for i in seq {
        // Inverted height. This puts tall bottles in front of smaller bottles in the prefix sum.
        let inv = max - i;

        // Add bottle in first level
        level1.add(inv, 1);

        // Count number of bottles twice as tall as 'i'
        // Add them to second level
        level2.add(inv, level1.prefix_sum(inv - i + 1));

        // Count number of bottles twice as tall as the bottles twice as tall as 'i'
        // Add them to final count
        count += level2.prefix_sum(inv - i + 1);
    }

    println!("{count}");
}
