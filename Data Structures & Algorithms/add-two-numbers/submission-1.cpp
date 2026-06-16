class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *l3 = nullptr;
        int carry = 0, sum;
        
        while (l1 != nullptr || l2 != nullptr) {
            sum = carry;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            carry = sum / 10;
            
            // Create a new node for the current digit
            ListNode* newnode = new ListNode(sum % 10);

            if (head == nullptr) {
                head = newnode;  // First node becomes the head
                l3 = head;
            } else {
                l3->next = newnode;  // Link the new node
                l3 = l3->next;
            }
        }

        // If there's a carry left after the final addition, add a new node
        if (carry > 0) {
            l3->next = new ListNode(carry);
        }

        return head;
    }
};
