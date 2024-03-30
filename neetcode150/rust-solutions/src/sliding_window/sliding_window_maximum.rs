use std::collections::VecDeque;

fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {

    let mut output = vec![];
    let mut q: VecDeque<usize> = VecDeque::new();

    let mut start = 0;
    let mut end = 0;

    while end < nums.len() {
        while !q.is_empty() && nums[end] > nums[*q.back().unwrap()] {
            q.pop_back();
        }

        q.push_back(end);

        if start > *q.front().unwrap() {
            q.pop_front();
        }

        if end + 1 >= k as usize {
            output.push(nums[*q.front().unwrap()]);
            start += 1;
        }

        end += 1;
    }

    output

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_sliding_window() {
        let nums = vec![1,3,-1,-3, 5,3,6,7];
        let k = 3;
        let want = vec![3,3,5,5,6,7];
        let got = max_sliding_window(nums, k);
        assert_eq!(got, want);
    }

    #[test]
    fn test_max_sliding_window_1() {
        let nums = vec![1];
        let k = 1;
        let want = vec![1];
        let got = max_sliding_window(nums, k);
        assert_eq!(got, want);
    }
}
