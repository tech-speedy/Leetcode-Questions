#define TABLE_SIZE 10000

typedef struct {
    int key;
    int value;
} HashItem;

int hash(int key) {
    return abs(key) % TABLE_SIZE;
}

void insert(HashItem* table[], int key, int value) {
    int idx = hash(key);
    while (table[idx] != NULL) {
        idx = (idx + 1) % TABLE_SIZE;
    }
    table[idx] = (HashItem*)malloc(sizeof(HashItem));
    table[idx]->key = key;
    table[idx]->value = value;
}

int find(HashItem* table[], int key) {
    int idx = hash(key);
    while (table[idx] != NULL) {
        if (table[idx]->key == key)
            return table[idx]->value;
        idx = (idx + 1) % TABLE_SIZE;
    }
    return -1;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashItem* table[TABLE_SIZE] = {0};
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int index = find(table, complement);
        if (index != -1) {
            result[0] = index;
            result[1] = i;
            return result;
        }
        insert(table, nums[i], i);
    }

    *returnSize = 0;
    return NULL;

}