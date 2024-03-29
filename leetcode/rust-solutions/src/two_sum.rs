use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut op_dict = HashMap::new();

    for i in 0..nums.len() {
        let num_2 = target - nums[i];
        if let Some(&value) = op_dict.get(&num_2) {
            return vec![i as i32, value];
        }
        op_dict.insert(nums[i], i as i32);
    }

    return vec![-1, -1];
}
