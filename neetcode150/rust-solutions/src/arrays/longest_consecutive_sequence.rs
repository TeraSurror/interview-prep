use std::collections::HashSet;

fn longest_consecutive_sequence(nums: Vec<i32>) -> i32 {
    let set: HashSet<i32> = HashSet::from_iter(nums.into_iter());
    let mut result = 0;

    for num in &set {
        if !set.contains(&(num - 1)) {
            let mut next = num + 1;
            let mut count = 1;
            while set.contains(&next) {
                next += 1;
                count += 1;
            }
            result = result.max(count);
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let nums = vec![100, 4, 200, 1, 3, 2];
        let result = 4;
        assert_eq!(longest_consecutive_sequence(nums), result);
    }

    #[test]
    fn test2() {
        let nums = vec![0, 3, 7, 2, 5, 8, 4, 6, 0, 1];
        let result = 9;
        assert_eq!(longest_consecutive_sequence(nums), result);
    }
}
