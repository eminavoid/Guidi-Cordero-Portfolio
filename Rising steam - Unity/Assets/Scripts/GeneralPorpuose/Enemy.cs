using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;
using UnityEngine.Events;

[RequireComponent(typeof(CircleCollider2D))]
[RequireComponent(typeof(Rigidbody2D))]

public class Enemy : MonoBehaviour
{
    [SerializeField] private BattleManager battleManager;
    [SerializeField] private float maxLife = 100;
    [SerializeField] private int armor = 1;
    [SerializeField] private int casillasAMover = 6;
    [SerializeField] private HealthBar barraDeVida;
    [SerializeField] private int enemyType = 0;
    [SerializeField] private int distPlayerMax = 1;
    [SerializeField] private int distPlayerMin = 1;
    [SerializeField] private float moveTime = 1;
    [SerializeField] private float rangeDamage;
    [SerializeField] private float meleeDamage;

    private GameObject player;
    private float life;
    private Animator animator;
    private List<GameObject> playerList;
    private float timer = 0;
    private float distPlayerY, distPlayerX, distPlayerTotal;
    private int casillasMovidas = 0;
    private Vector3 StartPos;
    private Vector3 LastPos;
    private float NearObstacleDist;
    private Vector3 NearObstacleDistVect;
    private Vector3 NearObstaclePos = new Vector3(100, 100, 100);
    private int myTurn;
    private bool isMyTurn = false;
    private bool right = true;
    private bool left = true;
    private bool up = true;
    private bool down = true;
    private int rightOrLeft = 0;
    private int upOrDown = 0;
    private int XorY = 0;
    private int focusPlayer;
    private bool canAttack = true;
    private bool isDead = false;

    private void OnTriggerEnter2D(Collider2D collision)
    {
        NearObstaclePos = collision.gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        if (NearObstacleDistVect == Vector3.right)
        {
            rightOrLeft = 1;
            right = false;
        }
        if (NearObstacleDistVect == Vector3.left)
        {
            rightOrLeft = 0;
            left = false;
        }
        if (NearObstacleDistVect == Vector3.up)
        {
            upOrDown = 1;
            up = false;
        }
        if (NearObstacleDistVect == Vector3.down)
        {
            upOrDown = 0;
            down = false;
        }
    }

    private void OnTriggerStay2D(Collider2D collision)
    {
        NearObstaclePos = collision.gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        if (NearObstacleDistVect == Vector3.right)
        {
            rightOrLeft = 0;
            right = false;
        }
        if (NearObstacleDistVect == Vector3.left)
        {
            rightOrLeft = 1;
            left = false;
        }
        if (NearObstacleDistVect == Vector3.up)
        {
            upOrDown = 0;
            up = false;
        }
        if (NearObstacleDistVect == Vector3.down)
        {
            upOrDown = 1;
            down = false;
        }
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        NearObstaclePos = collision.gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        if (NearObstacleDistVect != Vector3.right)
        {
            right = true;
        }
        if (NearObstacleDistVect != Vector3.left)
        {
            left = true;
        }
        if (NearObstacleDistVect != Vector3.up)
        {
            up = true;
        }
        if (NearObstacleDistVect != Vector3.down)
        {
            down = true;
        }
    }

    public void GetDamage(float attackDamage)
    {
        life -= attackDamage;
        barraDeVida.SetHealth();
    }

    public float maxlifePost()
    {
        return maxLife;
    }

    public float lifePost() 
    { 
        return life; 
    }

    public void changeTurn(bool turn)
    {
        isMyTurn = turn;
    }

    private void doDamage(GameObject player, int typeOfDamage)
    {
        RaycastHit2D[] hit = Physics2D.LinecastAll(gameObject.transform.position, player.gameObject.transform.position);
        RaycastHit2D[] hit2 = Physics2D.LinecastAll(player.gameObject.transform.position, gameObject.transform.position);

            if (hit[hit.Length-1].collider.gameObject.TryGetComponent<Player>(out Player component))
            {
                if (hit.Length >= 3 && typeOfDamage == 0)
                {
                    Debug.Log((((hit[hit.Length - 2].point - hit2[1].point).magnitude) / Mathf.Sqrt(2)));
                    float actualDamage = (rangeDamage - (rangeDamage * (((hit[hit.Length - 2].point - hit2[1].point).magnitude) / Mathf.Sqrt(2))));

                    component.GetDamage(actualDamage);
                    canAttack = false;
                }
                else if (hit.Length < 3 && typeOfDamage == 0)
                {
                    component.GetDamage(rangeDamage);
                    canAttack = false;
                }

                if (hit[hit.Length - 1].distance <= 1 && typeOfDamage == 1)
                {
                    component.GetDamage(meleeDamage);
                    canAttack = false;
                }

                if (component.lifePost() <= 0)
                {
                    //Debug.Log(focusPlayer);
                    component.killPlayer();
                    battleManager.popPlayersList(focusPlayer);
                    foreach (GameObject item in battleManager.EnemyListPost())
                    {
                        if (item.TryGetComponent<Enemy>(out Enemy enemigo))
                        {
                            enemigo.selectPlayer();
                        }
                    }
                }
            }
    }

    private void EnemyTurn()
    {
        //Debug.Log(myTurn);
        if (isMyTurn && playerList.Count != 0 && !isDead)
        {


            // Distancia al jugador (por ahora solo con un jugador)
            
            distPlayerY = playerList[focusPlayer].transform.position.y - gameObject.transform.position.y;
            distPlayerX = playerList[focusPlayer].transform.position.x - gameObject.transform.position.x;
            distPlayerTotal = Mathf.Sqrt((distPlayerX* distPlayerX)+(distPlayerY* distPlayerY));
            //Debug.Log(up);
            //Debug.Log(down);
            //Debug.Log(left); 
            //Debug.Log(right);
            //Debug.Log(rightOrLeft);
            //Debug.Log(upOrDown);

            // Movimiento de chase del enemigo
            // Condicion de movimiento
            if (distPlayerTotal > 1 && casillasAMover > casillasMovidas && timer > moveTime && distPlayerTotal > distPlayerMax)
            {
                //Debug.Log(casillasMovidas);
                // Random que dice si moverse para la derecha o para la izquierda


                if (distPlayerY != 0 && XorY == 0)
                {
                    if (Mathf.Sign(distPlayerY) == 1 && up)
                    {
                        transform.position = gameObject.transform.position + (Vector3.up);
                        casillasMovidas++;
                        timer = 0;
                    }else if (Mathf.Sign(distPlayerY) == -1 && down)
                    {
                        transform.position = gameObject.transform.position + (Vector3.down);
                        casillasMovidas++;
                        timer = 0;
                    }else if (right && rightOrLeft == 1)
                    {
                        transform.position = gameObject.transform.position + (Vector3.right);
                        casillasMovidas++;
                        timer = 0;
                    }else if (left && rightOrLeft == 0)
                    {
                        transform.position = gameObject.transform.position + (Vector3.left);
                        casillasMovidas++;
                        timer = 0;
                    }
                    
                } else
                {
                    XorY = 1;
                }
                
                if (distPlayerX !=0 && XorY == 1)
                {
                    if (Mathf.Sign(distPlayerX) == 1 && right)
                    {
                        transform.position = gameObject.transform.position + (Vector3.right);
                        casillasMovidas++;
                        timer = 0;
                    }
                    else if (Mathf.Sign(distPlayerX) == -1 && left)
                    {
                        transform.position = gameObject.transform.position + (Vector3.left);
                        casillasMovidas++;
                        timer = 0;
                    }
                    else if (up && upOrDown == 1)
                    {
                        transform.position = gameObject.transform.position + (Vector3.up);
                        casillasMovidas++;
                        timer = 0;
                    }
                    else if (down && upOrDown == 0)
                    {
                        transform.position = gameObject.transform.position + (Vector3.down);
                        casillasMovidas++;
                        timer = 0;
                    }


                }
                else
                {
                    XorY = 0;
                }
            }

            if (distPlayerTotal <= distPlayerMax && distPlayerTotal > 1 && canAttack) 
            {
                animator.SetTrigger("isMagic");
                AudioManager.instance.PlaySFX("Magic");
                doDamage(player, 0); 
            }
            if (distPlayerTotal <= 1 && canAttack)
            {
                animator.SetTrigger("isAttacking");
                AudioManager.instance.PlaySFX("Sword");
                doDamage(player, 1);
            }


            // Fin del turno
            if (casillasAMover == casillasMovidas || distPlayerTotal <= distPlayerMax)
            {
                battleManager.NextTurn();
                timer = 0;
                casillasMovidas = 0;
                canAttack = true;
                isMyTurn = false;
            }

            // Timer para que el movimiento del enemigo
            timer += Time.deltaTime;
        }
    }

    public void AssignTurn(int turn)
    {
        myTurn = turn;
    }
    public void killEnemy()
    {
        isDead = true;
    }

    private void Awake()
    {
        
        battleManager.EnemyPost(gameObject);
    }

    private void selectPlayer()
    {
        playerList = battleManager.PlayerListPost();
        if (playerList.Count != 0)
        {
            focusPlayer = UnityEngine.Random.Range(0, playerList.Count);
            player = playerList[focusPlayer];
        }
        
    }

    // Start is called before the first frame update
    void Start()
    {
        casillasMovidas = 0;
        canAttack = true;
        isMyTurn = false;
        life = maxLife;
        animator = GetComponent<Animator>();
        StartPos = gameObject.transform.position;
        LastPos = gameObject.transform.position;
        NearObstacleDistVect = NearObstaclePos - gameObject.transform.position;
        NearObstacleDist = NearObstacleDistVect.magnitude;
        selectPlayer();
    }

    // Update is called once per frame
    void Update()
    {
        if (!isDead)
        {
            EnemyTurn();
        }else if (isDead && battleManager.QueTurno() == myTurn)
        {
            battleManager.NextTurn();
        }
        Debug.Log(life);
    }
}
