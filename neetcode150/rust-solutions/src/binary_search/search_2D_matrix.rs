fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {

    fn search_1D(arr: &Vec<i32>, target: i32) -> bool {
        let mut start = 0;
        let mut end = arr.len();

        while start < end {
            let mid = start + (end - start) / 2;
            match target.cmp(&arr[mid]) {
                std::cmp::Ordering::Equal => return true,
                std::cmp::Ordering::Greater => start = mid + 1,
                std::cmp::Ordering::Less => end = mid,
            }
        }

        false
    }

    let mut start = 0;
    let mut end = matrix.len();

    while start < end {
        let mid = start + (end - start) / 2;

        let row_start = matrix[mid][0];
        let row_end = matrix[mid][matrix[0].len() - 1];

        if row_start <= target && target <= row_end {
            return search_1D(&matrix[mid], target);
        } else if row_start > target {
            end = mid;
        } else {
            start = mid + 1;
        }
    }
    
    false


}


