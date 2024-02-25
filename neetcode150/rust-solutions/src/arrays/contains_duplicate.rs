use std::collections::HashSet;

/*

Finds if a list contains duplicates or not.
Sol:
Create a HashSet
Iterate through the list, append if number is not in set
If num is in set, return true -> This means duplicate exists
return false if we iterate through the whole list.

*/
fn contains_duplicate(nums: Vec<i32>) -> bool {
    let mut set = HashSet::new();

    for num in nums {
        let curr_num = num;
        if set.contains(&curr_num) {
            return true;
        }
        set.insert(curr_num);
    }

    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_true() {
        let nums = vec![1, 2, 3, 1];
        assert!(contains_duplicate(nums));
    }

    #[test]
    fn test_false() {
        let nums = vec![1, 2, 3, 4];
        assert!(!contains_duplicate(nums));
    }
}
