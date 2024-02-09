using System.Collections;
using System.Collections.Generic;
using System.Drawing;
using Unity.VisualScripting;
using UnityEditor;
using UnityEngine;

public class ChestContainer : MonoBehaviour
{
    private Animator animator;
    private bool InChestRad;
    GameObject childPopUp;
    public bool InsideChestRaius()
    {
        return InChestRad;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        InChestRad = true;
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        InChestRad = false;
    }

    private void Start()
    {
        animator = GetComponent<Animator>();
    }
    private void ShowLoot ()
    {
        //GameObject parentObject = GameObject.Find("Chest 1");
        //Transform parentTransform = parentObject.transform;
        Transform child = this.gameObject.transform.GetChild(0);
        childPopUp = child.gameObject;
        StartCoroutine(ShowObjectForTime(5f));

    }
    IEnumerator ShowObjectForTime(float time)
    {
        childPopUp.SetActive(true);
        yield return new WaitForSeconds(time);
        childPopUp.SetActive(false);
        Destroy(childPopUp);
    }
    // Update is called once per frame
    void Update()
    {
        if (InChestRad && Input.GetButtonDown("Interact"))
        {
            ShowLoot();
            animator.SetTrigger("isOpening");
            
        }
        
    }
}