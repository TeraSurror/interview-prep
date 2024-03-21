use std::cmp::{max, min};

fn trap(height: Vec<i32>) -> i32 {
    let mut left = vec![0; height.len()];
    let mut right = vec![0; height.len()];

    left[0] = height[0];
    right[height.len() - 1] = height[height.len() - 1];

    for i in 1..height.len() {
       left[i] = max(height[i], left[i - 1]);
    }

    for i in (0..height.len() - 1).rev() { 
       right[i] = max(height[i], right[i + 1]);
    }

    let mut result = 0;

    for i in 0..height.len() {
        result += min(left[i] - height[i], right[i] - height[i]);
    }

    return result;
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_trap() {
        let height = vec![4, 2, 0, 3, 2, 5];
        let want = 9;
        let got = trap(height);
        assert_eq!(want, got);
    }

    #[test]
    fn test_trap1() {
        let height = vec![0,1,0,2,1,0,1,3,2,1,2,1];
        let want = 6;
        let got = trap(height);
        assert_eq!(want, got);
    }
}
