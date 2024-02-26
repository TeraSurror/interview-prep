use std::collections::HashMap;

fn top_k_freq(nums: Vec<i32>, k: i32) -> Vec<i32> {
    let mut result = Vec::new();

    let mut map: HashMap<i32, i32> = HashMap::new();
    let mut buckets = vec![Vec::new(); nums.len() + 1];

    for num in nums {
        *map.entry(num).or_default() += 1;
    }

    for (num, count) in map.into_iter() {
        buckets[count as usize].push(num);
    }

    let mut index = buckets.len() - 1;
    let mut count = 0;
    while index >= 1_usize && count < k {
        if buckets[index].len() > 0 {
            for num in &buckets[index] {
                result.push(*num);
                count += 1;
            }
        }
        index -= 1;
    }

    result
}
