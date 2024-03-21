use std::cmp::{max, min};

fn max_area(height: Vec<i32>) -> i32 {
    let mut left = 0;
    let mut right = height.len() - 1;
    let mut result = 0;


    while left < right {
        let area = min(height[left], height[right]) * (right - left) as i32;
        result = max(result, area as i32);
        if left > right {
            right -= 1;
        } else {
            left += 1;
        }
    }

    return result;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_area() {
        let height = vec![1, 8, 6, 2, 5, 4, 8, 3, 7];       
        let want = 49;
        let got = max_area(height);
        assert_eq!(want, got);
    }
}

