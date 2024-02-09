using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class InventoryItem
{
    public InventoryItemData ItemData;
    public int StackSize;

    public InventoryItem(InventoryItemData item)
    {
        ItemData = item;
        AddToStack(1);
    }
    public void AddToStack(int TimesToExecute)
    {
        for (int i = 0; i < TimesToExecute; i++)
        {
            StackSize++;
        }
    }
    public void RemoveFromStack(int TimesToExecute)
    {
        for (int i = 0; i < TimesToExecute; i++)
        {
            StackSize--;
        }
        
    }
}
