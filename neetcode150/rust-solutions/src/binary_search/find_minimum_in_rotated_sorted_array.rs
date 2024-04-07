fn find_min(nums: Vec<i32>) -> i32 {
    let length = nums.len();

    if length == 1 {
        return nums[0];
    }

    let mut start = 0;
    let mut end = length - 1;

    while start < end {
        let m = start + (end - start) / 2;

        let left = nums[start];
        let mid = nums[m]; 
        let right = nums[end];

        if left <= mid && mid <= right {
            return left;
        } else if left >= mid && mid >= right {
            return right;
        } else if left > mid || mid < right {
            end = m;
        } else {
            start = m;
        }
    }

    -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_min_1() {
        let nums = vec![3, 4, 5, 1, 2];
        let got = find_min(nums);
        let want = 1;
        assert_eq!(want, got);
    }

    #[test]
    fn test_find_min_2() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let got = find_min(nums);
        let want = 0;
        assert_eq!(want, got);
    }

    #[test]
    fn test_find_min_3() {
        let nums = vec![11, 13, 15, 17];
        let got = find_min(nums);
        let want = 11;
        assert_eq!(want, got);
    }
}

