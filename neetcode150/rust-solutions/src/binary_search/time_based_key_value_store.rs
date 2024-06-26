use std::collections::HashMap;

struct TimeMap {
    map: HashMap<String, Vec<(String, i32)>>
}

impl TimeMap {
    fn new() -> Self {
        TimeMap {
            map: HashMap::new(),  
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.map.entry(key).or_default().push((value, timestamp));
    }

    fn get(&mut self, key: String, timestamp: i32) -> String {
        let mut res = String::new();

        if let Some(t_list) = self.map.get(&key) {
            let (mut l, mut r) = (0, t_list.len() - 1);

            while l <= r {
                let m = l + (r - l) / 2;
                if timestamp < t_list[m].1 {
                    r = m - 1;
                } else {
                    res = t_list[m].0.clone();
                    l = m + 1;
                }
            }
        }

        res
    }
}
