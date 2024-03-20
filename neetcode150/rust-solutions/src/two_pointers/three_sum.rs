fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {

    let mut result: Vec<Vec<i32>> = Vec::new();

    nums.sort();

    for i in 0..nums.len() {
        if i > 0 && nums[i] == nums[i - 1] {
            continue;
        }

        let mut left = i + 1;
        let mut right = nums.len() - 1;

        while left < right {
            let total = nums[i] + nums[left] + nums[right];

            if total == 0 {
                result.push(vec![nums[i], nums[left], nums[right]]);
                left += 1;
                while nums[left] == nums[left - 1] && left < right {
                    left += 1;
                }
                right -= 1;
                while nums[right] == nums[right + 1] && left < right {
                    right -= 1;
                }
            } else if total < 0 {
               left += 1; 
            } else {
                right -= 1;
            }
        }
    }

    return result;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_three_sum_1() {
        let nums = vec![-1, 0, 1, 2, -1, 4];
        let got = three_sum(nums);
        let want = vec![vec![-1, -1, 2], vec![-1, 0, 1]];
        assert_eq!(got, want)
    }
}
