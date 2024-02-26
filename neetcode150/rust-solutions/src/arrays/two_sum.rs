use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = HashMap::new();

    for (i, num) in nums.into_iter().enumerate() {
        let diff = target - num;
        if map.contains_key(&diff) {
            let j = *map.get(&diff).unwrap();
            return vec![i as i32, j as i32];
        }
        map.insert(num, i);
    }

    vec![-1, -1]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let result = vec![1, 0];
        assert_eq!(two_sum(nums, target), result);
    }

    #[test]
    fn test_2() {
        let nums = vec![3, 2, 4];
        let target = 6;
        let result = vec![2, 1];
        assert_eq!(two_sum(nums, target), result);
    }

    #[test]
    fn test_3() {
        let nums = vec![3, 3];
        let target = 6;
        let result = vec![1, 0];
        assert_eq!(two_sum(nums, target), result);
    }
}
