fn search(nums: Vec<i32>, target: i32) -> i32 {
    let mut start = 0;
    let mut end = nums.len() - 1;

    while start <= end {
        let mid = start + (end - start) / 2;

        let left = nums[start];
        let middle = nums[mid];
        let right = nums[end];

        if target == middle {
            return mid as i32;
        } else if left < middle && middle < right {
            if target > middle {
                start = mid + 1;
            } else {
                end = mid - 1;
            }    
        } else if left > middle && middle < right {
            if middle < target && target <= right {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        } else {
            if left <= target && target < middle {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
    }
    
    -1
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_search_1() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let target = 0;
        let got = search(nums, target);
        let want = 4;
        assert_eq!(got, want);
    }

    #[test]
    fn test_search_2() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let target = 3;
        let got = search(nums, target);
        let want = -1;
        assert_eq!(got, want);
    }

    #[test]
    fn test_search_3() {
        let nums = vec![1];
        let target = 0;
        let got = search(nums, target);
        let want = -1;
        assert_eq!(got, want);
    }
}
