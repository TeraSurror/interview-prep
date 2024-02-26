/*
Watch this video: https://www.youtube.com/watch?v=bNvIQI2wAjk
*/
fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
    let n = nums.len();
    let mut prefix = nums[0];

    let mut output = vec![1; n];

    let mut index = 1;

    while index < n {
        let curr_num = nums[index];
        output[index] = prefix;
        prefix *= curr_num;
        index += 1;
    }

    prefix = nums[n - 1];
    index -= 2;
    loop {
        let curr_num = nums[index];
        output[index] *= prefix;
        prefix *= curr_num;
        if index == 0 {
            break;
        }
        index -= 1;
    }

    output
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let nums = vec![1, 2, 3, 4];
        let result = vec![24, 12, 8, 6];
        assert_eq!(product_except_self(nums), result);
    }

    #[test]
    fn test2() {
        let nums = vec![-1, 1, 0, -3, 3];
        let result = vec![0, 0, 9, 0, 0];
        assert_eq!(product_except_self(nums), result);
    }
}
