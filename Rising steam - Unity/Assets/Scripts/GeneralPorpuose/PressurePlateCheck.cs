using System.Collections;
using System.Collections.Generic;
//using UnityEditor.UIElements;
using UnityEngine;

public class PressurePlateCheck : MonoBehaviour
{
    private bool PlatePressed =  false;
    [SerializeField] public GameObject ChangedObject;
    private GameObject ObjectType;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        ObjectType = collision.gameObject;
        if (ObjectType.CompareTag("MovableObject"))
        {
            PlatePressed = true;
            Debug.Log(PlatePressed);
        }
    }
    private void OnTriggerExit2D(Collider2D collision)
    {
        ObjectType = collision.gameObject;
        if (ObjectType.CompareTag("MovableObject"))
        {
            PlatePressed = false;
            Debug.Log(PlatePressed);
        }
    }

    private void PlateAction()
    {
        if (PlatePressed)
        {
            ChangedObject.gameObject.SetActive(false);
        }
        if (!PlatePressed)
        {
            ChangedObject.gameObject.SetActive(true);
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        PlateAction();
    }
}
