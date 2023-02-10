function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

var addTwoNumbers = function(l1, l2) {
    let dummy = new ListNode(0);
    let cur = dummy;
    let carry = 0;
    
    while (l1 || l2 || carry) {
        if (l1) {
            carry += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            carry += l2.val;
            l2 = l2.next;
        }
        cur.next = new ListNode(carry % 10);
        cur = cur.next;
        carry = Math.floor(carry / 10);
    }
    
    return dummy.next;
};
