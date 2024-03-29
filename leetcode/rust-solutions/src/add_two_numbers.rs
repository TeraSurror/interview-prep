use crate::utils::linked_list::ListNode;

fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>>{

    let mut l1 = l1.as_ref();
    let mut l2 = l2.as_ref();

    let mut dummy = Box::new(ListNode::new(0));
    let mut curr = dummy.as_mut();

    let mut carry = 0;

    while l1.is_some() || l2.is_some() || carry > 0 {
        let val1 = l1.map(|n| n.val).unwrap_or_default();
        let val2 = l2.map(|n| n.val).unwrap_or_default();

        let sum = val1 + val2 + carry;
        carry = sum / 10;
        curr.next = Some(Box::new(ListNode::new(sum % 10)));
        curr = curr.next.as_mut().unwrap();

        if let Some(node) = l1 {
            l1 = node.next.as_ref();
        }

        if let Some(node) = l2 {
            l2 = node.next.as_ref();
        }
    }

    dummy.next

}
