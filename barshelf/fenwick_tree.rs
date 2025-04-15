use std::collections::HashMap;

fn greatest_power_below(i: usize) -> usize {
    let i = i as i64;
    (i & -i) as usize
}

type Int = u64;

pub struct FenwickTree {
    arr: HashMap<usize, Int>,
    max: usize,
}

impl FenwickTree {
    pub fn new(max: usize) -> Self {
        Self {
            arr: HashMap::new(),
            max,
        }
    }

    pub fn add(&mut self, mut i: usize, k: Int) {
        i += 1;
        while i < self.max {
            self.arr.entry(i).and_modify(|v| *v += k).or_insert(k);
            i += greatest_power_below(i)
        }
    }

    /// Sum until and excluding i
    pub fn prefix_sum(&self, mut i: usize) -> Int {
        let mut s = 0;
        while i > 0 {
            s += self.arr.get(&i).unwrap_or(&0);
            i -= greatest_power_below(i);
        }

        s
    }
}
