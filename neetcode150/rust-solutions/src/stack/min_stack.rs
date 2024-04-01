use std::collections::VecDeque;

struct MinStack {
    stack: VecDeque<i32>,
    min_stack: VecDeque<i32>,
}

impl MinStack {

    fn new() -> Self {
        let mut stack = VecDeque::new();
        let mut min_stack = VecDeque::new();
        
        MinStack {
            stack,
            min_stack
        }
    }

    fn push(&mut self, val: i32) {
        self.stack.push_back(val);
        if self.min_stack.len() == 0 || *self.min_stack.back().unwrap() >= val {
            self.min_stack.push_back(val);
        }
    }

    fn pop(&mut self) {
        let poped = self.stack.pop_back().unwrap();
        if poped == *self.min_stack.back().unwrap() {
            self.min_stack.pop_back();
        }
    }

    fn top(&self) -> i32 {
        *self.stack.back().unwrap()
    }

    fn get_min(&self) -> i32 {
        *self.min_stack.back().unwrap()
    }

}
