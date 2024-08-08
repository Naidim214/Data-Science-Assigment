{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bb5a1097-f3fd-4621-ad08-1380bd73fcaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nWrite a Python module named calculator.py containing functions for addition, subtraction,\\nmultiplication, and division.\\n'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Write a Python module named calculator.py containing functions for addition, subtraction,\n",
    "multiplication, and division.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4b8f2d99-ba37-424a-a8b7-b636b4bdd71e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculator.py\n",
    "\n",
    "def add(a,b):\n",
    "    return a+b\n",
    "def subtract(a,b):\n",
    "    return a-b\n",
    "def multiply(a,b):\n",
    "    return a*b\n",
    "def divide(a,b):\n",
    "    return a/b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38168a41-8c83-4ed5-81dc-a9dd1b6462be",
   "metadata": {},
   "outputs": [],
   "source": [
    "# usage\n",
    "if __name__==\"__main__\":\n",
    "    print(f'Addition:5 + 3 = {add(5,3)}')\n",
    "    print(f'Subtraction: 5 -3 = {subtract(5,3)}')\n",
    "    print(f'Multiplication: 5 * 3 = {multiply(5,3)}')\n",
    "    print(f'Division: "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
