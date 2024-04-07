use std::mem::swap;

fn find_median_sorted_arrays(mut nums1: Vec<i32>, mut nums2: Vec<i32>) -> f64 {
    let total = nums1.len() + nums2.len();

    let half = total / 2;

    if nums1.len() > nums2.len() {
        swap(&mut nums1, &mut nums2);
    }

    let mut left = 0;
    let mut right = nums1.len();

    while left <= right {
        let mid = left + (right - left) / 2;

        let pointer = half - mid;

        let base_left = if mid > 0 {
            nums1[mid - 1] as f64
        } else {
            f64::MIN
        };

        let base_right = if mid< nums1.len() {
            nums1[mid] as f64
        } else {
            f64::MAX
        };

        let ref_left = if pointer > 0 {
            nums2[pointer - 1] as f64
        } else {
            f64::MIN
        };

        let ref_right = if pointer < nums2.len() {
            nums2[pointer] as f64
        } else {
            f64::MAX
        };

        if base_left <= ref_right && ref_left <= base_right {
            if total % 2 == 1 {
                return base_right.min(ref_right);
            } else {
                return (base_left.max(ref_left) + base_right.min(ref_right)) / 2.0;
            }
        } else if base_left > ref_right {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    -1.0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_median_1() {
        let nums1 = vec![1, 3];
        let nums2 = vec![2];
        let want = 2.0;
        let got = find_median_sorted_arrays(nums1, nums2);
        assert_eq!(got, want);
    }

    #[test]
    fn test_median_2() {
        let nums1 = vec![1, 2];
        let nums2 = vec![3, 4];
        let want = 2.5;
        let got = find_median_sorted_arrays(nums1, nums2);
        assert_eq!(got, want);
    }
}
