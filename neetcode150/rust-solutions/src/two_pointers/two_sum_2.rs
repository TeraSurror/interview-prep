fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut start = 0;
    let mut end = numbers.len() - 1;

    while start <= end {
        let total = numbers[end] + numbers[start];
        if total == target {
            return vec![(start + 1) as i32, (end + 1) as i32];
        } else if total < target {
            start += 1;
        } else {
            end -= 1;
        }
    }

    return vec![-1, -1];
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum_1() {
        let got = two_sum(vec![2, 7, 11, 15], 9);
        let want = vec![1, 2];
        assert_eq!(want, got);
    }

    #[test]
    fn test_two_sum_2() {
        let got = two_sum(vec![2, 3, 4], 6);
        let want = vec![1, 3];
        assert_eq!(want, got);
    }

    #[test]
    fn test_two_sum_3() {
        let got = two_sum(vec![-1, 0], -1);
        let want = vec![1, 2];
        assert_eq!(want, got);
    }
}
