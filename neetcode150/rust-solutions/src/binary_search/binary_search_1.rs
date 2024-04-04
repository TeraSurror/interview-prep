fn search(nums: Vec<i32>, target: i32) -> i32 {
    let mut start = 0;
    let mut end = nums.len();

    while start < end {
        let mid = start + (end - start) / 2;
        if nums[mid] == target {
            return mid as i32;
        } else if nums[mid] < target {
            start = mid + 1;
        } else {
            end = mid;
        }
    }

    -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bs_1() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 9;
        let got = search(nums, target);
        let want = 4;
        assert_eq!(got, want);
    }

    #[test]
    fn test_bs_2() {
        let nums = vec![-1, 0, 3, 5, 9, 12];
        let target = 2;
        let got = search(nums, target);
        let want = -1;
        assert_eq!(got, want);
    }
}
