class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;  // base case: return the last node as the new head
        }

        // Recursively reverse the rest of the list
        ListNode* newHead = reverseList(head->next);

        // Reverse the current node's next pointer
        head->next->next = head;

        // Set the current node's next pointer to null to avoid cycle
        head->next = nullptr;

        // Return the new head
        return newHead;
    }
};
