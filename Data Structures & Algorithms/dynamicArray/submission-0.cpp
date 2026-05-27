class DynamicArray {
private:
    int *myArr;
    int capacity;
    int length;

public:

    DynamicArray(int capacity): capacity(capacity), length(0) {
        this->myArr = new int[this->capacity];
    }

    int get(int i) {
        return this->myArr[i];
    }

    void set(int i, int n) {
        this->myArr[i] = n;
    }

    void pushback(int n) {
        if (this->length == this->capacity)
        {
            this->resize();
        }

        this->myArr[this->length++] = n;
    }

    int popback() {
        return this->myArr[--this->length];
    }

    void resize() {
        this->capacity *= 2;
        int* temp = new int[this->capacity];

        for (int i = 0; i < this->length; i++)
        {
            temp[i] = this->myArr[i];
        }

        delete(this->myArr);
        this->myArr = temp;
    }

    int getSize() {
        return this->length;
    }

    int getCapacity() {
        return this->capacity;
    }
};
